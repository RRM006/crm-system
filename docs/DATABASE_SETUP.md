# Database Setup Documentation

## Database Provider
**Supabase** (PostgreSQL)

## Connection Details
⚠️ Credentials are stored in `database-credentials.txt` (NOT uploaded to GitHub)

## Database Schema

### Tables Created:
1. **users** - System users with role-based access
2. **customers** - Customer/client information
3. **leads** - Sales leads and opportunities
4. **activities** - Calls, emails, meetings, tasks
5. **complaints** - Customer issues and tickets
6. **products** - Product catalog

### User Roles:
- admin
- sales_executive
- support_agent
- manager
- customer

## Setup Date
[31/10/25]

## Status
✅ Database created
✅ Tables created
✅ Test admin user added

## Next Steps
- Connect Django backend to database
- Create API endpoints
- Setup authentication