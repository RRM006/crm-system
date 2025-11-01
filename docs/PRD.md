![][image1]

**Department of Electrical and Computer Engineering**  
**North South University**

**CSE 327 Software Engineering**  
**Product Requirements Document**   
**ON**  
**Customer Relationship Management System (CRM)**

 Foysal Hasan Shifat		 2222347042  
Humaira Afia Anam		2231974642  
Rafiur Rahman Mashrafi       2221971042  
Marzia Hossain		        2222465642

**Faculty Advisor:**  
**Dr. Nabeel Mohammed**  
**Associate Professor**  
**ECE Department**  
**Fall, 2025**

##  **Overview**

The primary purpose of this Customer Relationship Management (CRM) System is to create a single, easy-to-use platform where businesses can manage all their customer interactions, sales activities, communications, and service requests in one place.

It supports B2B (Business-to-Business) and B2C (Business-to-Consumer) operations. It is suitable for large companies with multiple brands or divisions—such as Walton, Singer, or RFL—to work together under one unified system.

The CRM will be available as a web application and an Android mobile app, allowing users to access data and manage operations anytime, anywhere, with real-time updates across all devices.

###  **Vision & Goals**

* Centralize customer communication channels (calls, emails, chat, and voice).  
* Automate daily business tasks like mail sorting, lead follow-up, and complaint tracking.  
* Improve the efficiency of sales and support teams through better coordination.  
* Offer data-driven insights and analytics for decision-making.  
* Support both internal users and external customers (B2C portal).  
* Provide a scalable architecture that allows adding new modules like AI, bots, and an integration server.

###  **User Goals**

* Simplify daily CRM operations like lead tracking, communication, and reporting.  
* Access the system anytime from the web or the mobile app.  
* Enable quick communication via chat, email, or call.  
* Manage customer histories and issue resolutions from a single interface.  
* Receive timely notifications and reminders for tasks, follow-ups, or pending complaints.  
* Gain access to dashboards showing their KPIs and performance.

## **Success Evaluation**

## **Linked Objectives**

To measure success, the system will track improvements in performance and adoption rate:

* Reduce customer complaint resolution time by 40%.  
* Increase lead-to-sale conversion rate by 25%.  
* Improve team productivity and response speed.  
* Minimize data entry errors by automating repetitive processes.

### **Key Performance Indicators (KPIs)**

* Number of active users per department.  
* Average response and resolution time.  
* Number of leads generated and converted.  
* Uptime of CRM services (target: 99%).  
* Customer satisfaction score (CSAT).

### **Metrics That Should Not Change**

* Data privacy and integrity must remain uncompromised.  
* System latency should stay below 2 seconds per request.  
* Feature updates must not affect backward compatibility.

## **Success Metrics**

*  Response time by 40%

* 95% accuracy in multi-channel tracking

* 80% user adoption in 1 month.

* \+30% customer satisfaction

## **Target Audience (Users)**

### **User Categories**

1. **Admin:**  
    Responsible for managing user accounts, roles, permissions, and system configurations.  
2. **Sales Executive:**  
    Manages leads, opportunities, deals, and tracks communication with clients.  
3. **Customer Support Agent:**  
    Handles complaints, tickets, and post-sale service requests.  
4. **Manager / Supervisor:**  
    Monitors analytics, performance reports, and oversees team operations.  
5. **Customer (External):**  
    End-users who submit complaints, queries, or product feedback.

### **Problem statements:**

* Difficulty tracking communication across multiple channels.  
* Lack of integration between mail, call, and chat.  
* Time-consuming manual lead updates.  
* Inconsistent follow-ups lead to customer dissatisfaction.

### 

### **Needs and Jobs-to-Be-Done**

* A centralized dashboard for all communication.  
* Easy mobile access for field agents.  
* Real-time analytics to assess sales and service performance.  
* Auto-sorting customer emails into relevant categories (complaint, inquiry, etc.).

### **Research & Proof**

Existing businesses rely heavily on spreadsheets or manual methods for tracking leads and customer communication. This CRM will automate and standardize those processes.

## **Proposed Solution**

### **High-Level Overview**

The proposed CRM will be a Django-based web and mobile platform with integrated communication, data management, and analytics.  
It will include automated email sorting, voice chat, complaint tracking, and AI assistance.

**Phase 1: Build all functional modules (30+ features).**  
**Phase 2: Add Telegram bot, AI assistant, and MCP server.**

**Feature Prioritization Criteria**

* High Priority: Core CRM functions.  
* Medium Priority: Reporting and analytics.  
* Low Priority: AI & automation (Phase 2).

## 

## 

## 

## 

## **Project Scope**

### **Features Included (30+ Functional Requirements)**

#### ***Phase 1 (Core CRM System)***

## ***1\. Communication Features***

**Call from web and mobile (two-way communication).** You can make and receive calls directly through the website or mobile app like a phone.

**Automated email sorting using rules and AI filters.** Emails automatically organize themselves into folders based on rules you set or smart AI that learns what matters to you.

**Conversational text-based interface** Chat with the system like you're texting a friend – simple, natural conversations instead of complicated forms.

 **Voice chat feature:** Talk to customers or team members using voice messages or live voice calls within the app.

## **2\. Access & Security**

**Multi-client access (Walton, Singer, RFL, etc.)** Different companies can use the same system while keeping their data separate.

 **Role-based access management:** Control who sees what – managers see everything, salespeople see sales data, support staff see customer issues.

**Single account supporting multiple brands.** Manage several brands (like Walton and Singer) from one login without switching accounts.

 **User management and permission settings:** Add or remove team members and decide what each person can do in the system.

## **3\. Customer Management**

**Customer profile management:** Store all customer information in one place – contact details, purchase history, preferences, and notes.

 **Lead creation, tracking, and follow-up.** Keep track of potential customers, set reminders to contact them, and monitor their journey to becoming buyers.

**Task and activity management:** Create to-do lists, assign tasks to team members, and track what needs to be done.

**Complaint and issue management system:** Record customer problems, assign them to the right person, and track until they're solved.

## **4\. Monitoring & Reporting**

**Dashboard with real-time analytics:** See live updates of sales, customer activity, and team performance in easy-to-read charts and numbers.

**Reports and analytics for sales and support.** Generate detailed reports showing how well your sales and support teams are performing.

**Activity log and audit trail:** See a complete history of who did what and when. This helps track changes and accountability.

## **5\. Notifications & Reminders**

 **Notification system (email, push, SMS):** Get alerts through email, phone notifications, or text messages when something important happens.

**Calendar and reminder integration:** Sync with your calendar and get reminders for meetings, follow-ups, and deadlines.

## **6\. Sales Tools**

**Deal pipeline and stage tracking:** Visualize where each sale is in the process (initial contact → negotiation → closed deal).

**Product catalog management:** Maintain a list of all products with prices, descriptions, and images that everyone can access.

## **7\. Search & Organization**

**Search and filter options:** Quickly find customers, products, or deals using keywords and filters (like searching on Google).

**Data export (CSV/PDF)** Download your data as spreadsheets or PDF files to use in other programs or share with others.

## 

## 

## **8\. Collaboration**

**Document upload and sharing.** Upload files (contracts, images, documents) and share them with team members or customers.

**Chat module for internal communication.** Message your coworkers directly within the system without using separate chat apps.

## **8\. Global & Mobile Features**

**Multi-language support:** Use the system in different languages (Bengali, English, etc.) based on user preference.

**Mobile synchronization with offline support.** Work on your phone even without internet – changes sync automatically when you're back online.

## **9\. Technical Features**

**API for integration with third-party services.** Connect the system with other tools you use (like accounting software or email platforms).

**Integration with an open-source issue tracking API.** Link with external systems that track technical problems or customer issues.

**Data backup and restore:** Automatically save copies of all data so nothing is lost if something goes wrong – you can recover everything.

## **10\. Data Protection**

**Data backup and restore** automatically save copies of all your information regularly. If something breaks or data gets deleted, you can return everything to how it was, like it never happened.

## **11\. Customer Feedback**

**Feedback collection and survey module:** Send surveys to customers asking about their experience, collect their responses, and see the results in one place. Like Google Forms but built into your system.

## **12\. Security**

**Secure authentication (JWT/OAuth2)** is an Advanced security technology that keeps accounts safe. It's like having a special digital key that proves you're really you when logging in, making it very hard for hackers to break in.

#### ***Phase 2 (Advanced Integrations*****)**

**Instant Communication**

**1\. Telegram Bot for instant notifications.** Get essential alerts directly in your Telegram app – like when a new customer complaint or a deal is closed—no need to constantly check the system.

**2\. Artificial Intelligence**

**AI assistant for auto-email replies and chat summarization**

* **Auto-email replies:** AI reads incoming emails and automatically sends appropriate responses (like "We received your message and will reply within 24 hours").  
* **Chat summarization:** AI reads long conversations and creates a summary so you can understand what happened without reading everything.

**3\. MCP Server for managing multiple brands or business clients**

#### An innovative system that helps AI understand the specific context and information for each brand you manage. It ensures that when the AI assistant helps with Walton, it knows Walton's products, policies, and data – and when it switches to Singer, it automatically knows Singer's information instead. Think of it like giving the AI a different "brain" for each company so it always gives accurate, brand-specific responses. 

### **Possible Future integrations**

* Payment processing.  
* Social media analytics.  
* Third-party marketing automation tools.

## 

## **Product Details & Workflow**

### **End-to-End User Experience**

1. User logs in using secure credentials.  
2. Dashboard shows all activities — leads, issues, calls, and emails.  
3. Sales executives manage customer pipelines and add notes.  
4. Support agents handle complaints and mark them resolved.  
5. Managers track KPIs and generate reports.  
6. Admin manages access, permissions, and system logs.  
7. Telegram bot sends quick alerts.  
8. AI suggests replies and summarizes chat/email threads.

### **Concept Diagram (Described)**

* Frontend (React \+ Android App) → API → Django Backend → Database (PostgreSQL/Firebase)  
* AI and Bot modules run as microservices connected via API.

### **User Stories**

1. As a sales executive, I can view and update lead details from my phone.  
2. As a manager, I can generate daily and weekly reports.  
3. As a customer, I can log complaints via app or email.  
4. As an admin, I can add new employees and assign roles.

### **Conditions for User Acceptance**

* The app should sync instantly between the web and mobile.  
* Response time must be under 2 seconds.  
* Email automation accuracy above 90%.  
* AI summarization with at least 70% accuracy.

### 

### **Analytics & Event Tracking**

* Track login frequency, module usage, and task completion rate.  
* Google Analytics (web) \+ Kotlin or Java (mobile).

| Phase | Task | Duration |
| :---: | :---: | :---: |
| Phase 1 | Design, Backend, Frontend Development | 1st week |
| Phase 1 | Testing and QA | 2nd week |
| Phase 2 | AI, Telegram Bot, MCP Server Integration | 3rd week |
| Phase 2 | Beta Testing & Launch | 4th week |

## 

## 

## **Key Dependencies**

* Tech Stack: Django (backend), React (frontend), Kotlin (Android).  
* Database: PostgreSQL  
* APIs: Open-source issue tracking, Telegram API, and AI NLP API.  
* Hosting: Render / Vercel / Firebase free-tier.  
* Tools: GitHub, Postman, Docker.


## 

## **Potential Risks & Solutions**

| Risk | Description | Mitigation |
| :---: | :---: | :---: |
| Data loss | Server crash or accidental deletion | Daily auto-backups |
| Downtime | Hosting outage | Multi-server setup |
| Integration failure | Telegram or the AI API is not working | Use fallback modules |
| User adoption issues | Complex UI | Simplify design, provide tutorials |

## **Launch and Delivery Plan**

1. Internal testing and bug fixing.  
2. Beta release for 2–3 sample clients.  
3. Collect feedback and optimize UI.  
4. Final deployment on public server.  
5. Continuous updates every quarter.

## **Customer Support & Training Strategy**

* Provide user manuals and onboarding guides.  
* Offer video tutorials for all roles.  
* Include chatbot support for common questions.  
* Collect feedback via surveys and helpdesk tickets.

## 

## **Data Protection / Legal Compliance**

* Use HTTPS, JWT authentication, and database encryption.  
* Comply with GDPR and local privacy laws.  
* Use role-based permissions for access control.  
* Maintain regular vulnerability scans.

## **References & Supporting Material**

* Django official documentation.  
* React and Kotlin developer guides.  
* Telegram Bot API documentation.  
* Open-source AI libraries (e.g., spaCy, Hugging Face).  
* Firebase and Render hosting documentation.

## **Terminology Definition (Glossary)**

* CRM: Customer Relationship Management  
* MCP: Multi Client Platform  
* API: Application Programming Interface  
* KPI: Key Performance Indicator  
* B2B/B2C: Business-to-Business / Business-to-Consumer  
* JWT: JSON Web Token  
* GDPR: General Data Protection Regulation

## 

## 

## 

## 

## **Tools & Technologies (Proposed)**

| Component | Suggested Tools |
| :---: | :---: |
| Backend | Python (Django / Flask) |
| Frontend | React.js / Angular |
| Database | PostgreSQL / MongoDB |
| Email Integration | Gmail API, SMTP, IMAP |
| Call Integration | Twilio API or WebRTC |
| AI / NLP | OpenAI API, Hugging Face, Rasa (for chatbot) |
| Deployment | Docker, AWS / Azure |
| Version Control | GitHub |

**Approval Signatures**

| Role | Name | Date | Signature |
| ----- | ----- | ----- | ----- |
| Product Owner  |  |  |  |
| Engineering Lead  |  |  |  |
| Design Lead  |  |  |  |
| Stakeholder | Dr. Nabeel Mohammed |  |  |

[image1]: <data:image/png;base64,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>