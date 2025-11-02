# Mobile App (Android - Kotlin)

This is a beginner-friendly path to build the Android app and generate an APK.

## What you'll build (Phase 1)
- Login screen (email/password)
- Customers list screen (fetch from backend)

## Prerequisites
- Install Android Studio (latest)
- Min SDK 24, Target SDK latest

## Steps – create the project (10 minutes)
1. Open Android Studio > New Project > Empty Activity
2. Name: CRM Mobile, Package: com.example.crm, Language: Kotlin
3. Finish

## Add dependencies (app/build.gradle)
In `dependencies {}` add:
```
implementation("com.squareup.retrofit2:retrofit:2.11.0")
implementation("com.squareup.retrofit2:converter-gson:2.11.0")
implementation("com.squareup.okhttp3:logging-interceptor:4.12.0")
implementation("androidx.recyclerview:recyclerview:1.3.2")
implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.8.4")
```

## API client
Create `api/Api.kt`:
```kotlin
package com.example.crm.api

import okhttp3.Interceptor
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object Api {
    // Change to your deployed backend base URL
    var baseUrl = "http://10.0.2.2:8000/api/" // Android emulator -> localhost
    var token: String? = null

    private val authInterceptor = Interceptor { chain ->
        val req = chain.request().newBuilder().apply {
            token?.let { header("Authorization", "Bearer $it") }
        }.build()
        chain.proceed(req)
    }

    private val client = OkHttpClient.Builder()
        .addInterceptor(HttpLoggingInterceptor().apply { level = HttpLoggingInterceptor.Level.BASIC })
        .addInterceptor(authInterceptor)
        .build()

    fun <T> create(service: Class<T>): T = Retrofit.Builder()
        .baseUrl(baseUrl)
        .addConverterFactory(GsonConverterFactory.create())
        .client(client)
        .build()
        .create(service)
}
```

`api/Services.kt`:
```kotlin
package com.example.crm.api

import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

data class TokenReq(val email: String, val password: String)
data class TokenRes(val access: String, val refresh: String)
data class Customer(val id:Int, val first_name:String, val last_name:String?, val email:String?, val updated_at:String)
data class Page<T>(val results: List<T>?)

interface AuthService {
    @POST("auth/token/")
    suspend fun token(@Body body: TokenReq): TokenRes
}

interface CustomerService {
    @GET("customers/")
    suspend fun list(): Page<Customer>
}
```

## MainActivity (simple UI)
Replace `MainActivity.kt`:
```kotlin
package com.example.crm

import android.os.Bundle
import android.widget.*
import androidx.activity.ComponentActivity
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.crm.api.*
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val email = findViewById<EditText>(R.id.email)
        val pass = findViewById<EditText>(R.id.password)
        val login = findViewById<Button>(R.id.loginBtn)
        val list = findViewById<RecyclerView>(R.id.list)
        val status = findViewById<TextView>(R.id.status)

        list.layoutManager = LinearLayoutManager(this)
        val adapter = CustomerAdapter()
        list.adapter = adapter

        login.setOnClickListener {
            lifecycleScope.launch {
                try {
                    val auth = Api.create(AuthService::class.java)
                    val t = auth.token(TokenReq(email.text.toString(), pass.text.toString()))
                    Api.token = t.access
                    status.text = "Logged in"

                    val cs = Api.create(CustomerService::class.java)
                    val page = cs.list()
                    adapter.items = page.results ?: emptyList()
                    adapter.notifyDataSetChanged()
                } catch (e: Exception) {
                    status.text = "Error: ${e.message}"
                }
            }
        }
    }
}

class CustomerAdapter: RecyclerView.Adapter<CustomerVH>() {
    var items: List<Customer> = emptyList()
    override fun onCreateViewHolder(parent: android.view.ViewGroup, viewType: Int): CustomerVH {
        val v = android.view.LayoutInflater.from(parent.context).inflate(android.R.layout.simple_list_item_2, parent, false)
        return CustomerVH(v as android.widget.TwoLineListItem)
    }
    override fun getItemCount() = items.size
    override fun onBindViewHolder(holder: CustomerVH, position: Int) {
        val c = items[position]
        holder.view.text1.text = "${c.first_name} ${c.last_name ?: ""}"
        holder.view.text2.text = c.email ?: ""
    }
}

class CustomerVH(val view: android.widget.TwoLineListItem): RecyclerView.ViewHolder(view)
```

## activity_main.xml
Create `app/src/main/res/layout/activity_main.xml`:
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">
    <EditText android:id="@+id/email" android:hint="Email" android:layout_width="match_parent" android:layout_height="wrap_content" />
    <EditText android:id="@+id/password" android:hint="Password" android:inputType="textPassword" android:layout_width="match_parent" android:layout_height="wrap_content" />
    <Button android:id="@+id/loginBtn" android:text="Login & Fetch Customers" android:layout_width="match_parent" android:layout_height="wrap_content" />
    <TextView android:id="@+id/status" android:layout_width="match_parent" android:layout_height="wrap_content" />
    <androidx.recyclerview.widget.RecyclerView android:id="@+id/list" android:layout_width="match_parent" android:layout_height="0dp" android:layout_weight="1" />
    
</LinearLayout>
```

## Run
1) Make sure backend is running and reachable. On emulator use http://10.0.2.2:8000, on device use your PC IP.
2) Click Run ▶ or Build > Build APK(s).
3) Install the APK on your phone to test.

If login works on mobile and customers load, your web and mobile share the same database.
