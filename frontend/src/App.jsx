import React, { useEffect, useState } from 'react'
import { Routes, Route, Link, useNavigate } from 'react-router-dom'
import { api, setAuthToken } from './api'

function useAuth() {
  const [token, setToken] = useState(localStorage.getItem('token'))
  const navigate = useNavigate()

  const logout = () => {
    setAuthToken(null)
    setToken(null)
    navigate('/login')
  }

  return { token, setToken: (t) => { setAuthToken(t); setToken(t) }, logout }
}

function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const auth = useAuth()
  const navigate = useNavigate()

  const submit = async (e) => {
    e.preventDefault()
    setError('')
    try {
      const { data } = await api.post('/auth/token/', { email, password })
      auth.setToken(data.access)
      navigate('/customers')
    } catch (err) {
      setError(err.response?.data?.detail || 'Login failed')
    }
  }

  return (
    <div className="container py-5" style={{ maxWidth: 420 }}>
      <h3>Login</h3>
      <form onSubmit={submit}>
        <div className="mb-3">
          <label className="form-label">Email</label>
          <input className="form-control" value={email} onChange={e=>setEmail(e.target.value)} />
        </div>
        <div className="mb-3">
          <label className="form-label">Password</label>
          <input type="password" className="form-control" value={password} onChange={e=>setPassword(e.target.value)} />
        </div>
        {error && <div className="alert alert-danger">{error}</div>}
        <button className="btn btn-primary w-100" type="submit">Login</button>
        <div className="mt-2">
          <Link to="/register">No account? Register</Link>
        </div>
      </form>
    </div>
  )
}

function Register() {
  const [form, setForm] = useState({
    username:'', email:'', password:'', first_name:'', last_name:'', role:'CUSTOMER'
  })
  const [msg, setMsg] = useState('')
  const [error, setError] = useState('')
  const navigate = useNavigate()
  const submit = async (e) => {
    e.preventDefault()
    setMsg(''); setError('')
    try {
      await api.post('/auth/register/', form)
      setMsg('Registered! You can login now.')
      setTimeout(()=>navigate('/login'), 800)
    } catch (err) {
      setError('Registration failed')
    }
  }
  const set = (k) => (e) => setForm({ ...form, [k]: e.target.value })
  return (
    <div className="container py-5" style={{ maxWidth: 520 }}>
      <h3>Register</h3>
      <form onSubmit={submit}>
        <div className="row">
          <div className="col-md-6 mb-3"><label className="form-label">First Name</label><input className="form-control" onChange={set('first_name')} /></div>
          <div className="col-md-6 mb-3"><label className="form-label">Last Name</label><input className="form-control" onChange={set('last_name')} /></div>
        </div>
        <div className="mb-3"><label className="form-label">Email</label><input className="form-control" onChange={set('email')} /></div>
        <div className="mb-3"><label className="form-label">Username</label><input className="form-control" onChange={set('username')} /></div>
        <div className="mb-3"><label className="form-label">Password</label><input type="password" className="form-control" onChange={set('password')} /></div>
        <div className="mb-3"><label className="form-label">Role</label>
          <select className="form-select" onChange={set('role')}> 
            <option value="CUSTOMER">Customer</option>
            <option value="SALES">Sales Executive</option>
            <option value="SUPPORT">Customer Support</option>
            <option value="MANAGER">Manager/Supervisor</option>
            <option value="ADMIN">Admin</option>
          </select>
        </div>
        {msg && <div className="alert alert-success">{msg}</div>}
        {error && <div className="alert alert-danger">{error}</div>}
        <button className="btn btn-primary w-100" type="submit">Create account</button>
      </form>
    </div>
  )
}

function Customers() {
  const [items, setItems] = useState([])
  const [form, setForm] = useState({ first_name:'', last_name:'', email:'' })
  const [error, setError] = useState('')
  const auth = useAuth()

  useEffect(()=>{
    api.get('/customers/').then(r=> setItems(r.data.results || r.data)).catch(()=>setError('Load failed'))
  },[])
  const set = (k)=>e=> setForm({ ...form, [k]: e.target.value })
  const add = async (e)=>{
    e.preventDefault()
    try {
      const { data } = await api.post('/customers/', form)
      setItems([data, ...items])
      setForm({ first_name:'', last_name:'', email:'' })
    } catch(e){ setError('Create failed (check role/permissions)') }
  }
  return (
    <div className="container py-4">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h3>Customers</h3>
        <Link className="btn btn-outline-secondary" to="#" onClick={auth.logout}>Logout</Link>
      </div>
      <form className="row g-2 mb-3" onSubmit={add}>
        <div className="col"><input className="form-control" placeholder="First name" value={form.first_name} onChange={set('first_name')} /></div>
        <div className="col"><input className="form-control" placeholder="Last name" value={form.last_name} onChange={set('last_name')} /></div>
        <div className="col"><input className="form-control" placeholder="Email" value={form.email} onChange={set('email')} /></div>
        <div className="col-auto"><button className="btn btn-primary" type="submit">Add</button></div>
      </form>
      {error && <div className="alert alert-danger">{error}</div>}
      <table className="table table-striped">
        <thead><tr><th>Name</th><th>Email</th><th>Updated</th></tr></thead>
        <tbody>
          {items.map(c=> (
            <tr key={c.id}><td>{c.first_name} {c.last_name}</td><td>{c.email}</td><td>{new Date(c.updated_at).toLocaleString()}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default function App(){
  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container">
          <Link className="navbar-brand" to="/">CRM</Link>
          <div className="navbar-nav">
            <Link className="nav-link" to="/login">Login</Link>
            <Link className="nav-link" to="/register">Register</Link>
            <Link className="nav-link" to="/customers">Customers</Link>
          </div>
        </div>
      </nav>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/customers" element={<Customers />} />
      </Routes>
    </>
  )
}
