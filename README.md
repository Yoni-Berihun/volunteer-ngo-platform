# Volunteer & NGO Connection Platform

A mobile platform connecting volunteers with verified NGOs.

## Tech Stack
- Frontend: Flutter
- Backend: FastAPI
- Database: PostgreSQL

## Structure
/frontend - Flutter mobile app  
/backend  - FastAPI backend




# 🏗 Full Development Workflow: Step-by-Step

 **finished the database models**, so we’re at the **backend foundation stage**.

---

## **PHASE 1 — Backend Setup**

### **Step 1: Database & Tables**

* ✅ Already done: Models created with SQLAlchemy.
* **Next**:

  * Create `database.py` (DB engine & session)
  * Make sure PostgreSQL is running (local or Render)
  * Run `Base.metadata.create_all(bind=engine)` in `main.py` to generate tables
  * Optional: Integrate **Alembic** for migrations (recommended for future updates)

---

### **Step 2: Create Pydantic Schemas**

* Location: `app/schemas/`
* Purpose:

  * Define **request/response formats**
  * Separate API input from DB models (security + validation)
* Example schemas:

  * `UserCreate`, `UserResponse`
  * `VolunteerProfileCreate`, `VolunteerProfileResponse`
  * `OrganizationProfileCreate`, `OrganizationProfileResponse`
  * `OpportunityCreate`, `OpportunityResponse`
  * `ApplicationCreate`, `ApplicationResponse`

---

### **Step 3: Create Repositories (CRUD layer)**

* Location: `app/repositories/`
* Purpose:

  * Encapsulate all database queries
  * Keep your services clean
* Example functions:

  * `get_user_by_email(db, email)`
  * `create_volunteer_profile(db, data)`
  * `create_opportunity(db, org_id, data)`
  * `get_applications_for_volunteer(db, volunteer_id)`

---

### **Step 4: Create Services (Business Logic)**

* Location: `app/services/`
* Purpose:

  * Implement rules & logic:

    * Apply to opportunity
    * Check availability / skill matching
    * Handle badges (certificate, stipend)
    * Enforce phone visibility rules
    * Handle optional images (carousel / default)
* Services use **repositories** internally

---

### **Step 5: Authentication & Authorization**

* Location: `app/auth/`
* Tasks:

  * JWT login/register
  * Password hashing (bcrypt)
  * Role-based access: VOLUNTEER, ORGANIZATION, ADMIN
  * Protect endpoints using `Depends(get_current_user)`
* Make sure volunteers cannot edit orgs, orgs cannot edit volunteers, etc.

---

### **Step 6: Routers / API Endpoints**

* Location: `app/routers/`
* Tasks:

  * Organize endpoints by resource:

    * `/auth` → login, register
    * `/volunteers` → profile, applications
    * `/organizations` → profile, images, opportunities
    * `/opportunities` → list, detail, badges
    * `/applications` → apply, update status
  * Use **Pydantic schemas** for validation
  * Use **Services** for business logic

---

### **Step 7: File/Image Upload**

* Tasks:

  * Profile images
  * Organization carousel images
  * Opportunity images
* Options:

  * Save in `/media` locally during development
  * Or use **cloud storage** (AWS S3, Firebase Storage) for production
* Backend returns **URLs** to Flutter app

---

### **Step 8: Test Backend**

* Tools:

  * FastAPI **interactive Swagger docs** (`http://127.0.0.1:8000/docs`)
  * Postman for endpoint testing
* Make sure:

  * CRUD works
  * Relationships work
  * Authentication + roles enforced
  * Optional images / default image logic works

---

## **PHASE 2 — Frontend Setup (Flutter)**

### **Step 1: Flutter Project Structure**

* `lib/`

  * `models/` → Dart classes matching Pydantic schemas
  * `services/` → API calls to backend
  * `screens/` → UI screens
  * `widgets/` → reusable widgets
  * `main.dart` → entry point

---

### **Step 2: API Integration**

* Connect Flutter app to FastAPI backend
* Use **HTTP client / Dio**
* Tasks:

  * Login / Register
  * Fetch volunteer/organization profiles
  * Fetch opportunities list
  * Apply to opportunities
  * Upload images

---

### **Step 3: UI Implementation**

* Key screens:

  * Login / Register
  * Volunteer dashboard
  * Organization dashboard
  * Opportunities feed

    * Cards with title, image, badges
    * Tap → details with certificate/stipend badge
  * Profile screens (volunteer/org)

    * Optional images carousel for organizations
* Mobile-first design, clean & responsive

---

### **Step 4: State Management**

* Options:

  * Provider / Riverpod / Bloc
* Manage:

  * Logged-in user state
  * Opportunities list
  * Applications status
  * Image uploads

---

### **Step 5: Local Storage**

* Save JWT token securely on device
* Cache data if needed for offline use

---

### **Step 6: Testing Frontend**

* Functional testing of all screens
* Test API integration (apply, upload, badges, images)

---

## **PHASE 3 — Deployment**

### **Step 1: Backend Deployment**

* Options:

  * Render (easy)
  * Heroku / Railway / AWS
* Tasks:

  * Set `DATABASE_URL` in environment variables
  * Migrate DB tables
  * Serve FastAPI app with `uvicorn` or `gunicorn + uvicorn workers`

---

### **Step 2: Frontend Deployment**

* Flutter mobile app:

  * Android → Play Store
  * iOS → App Store
* Tasks:

  * Update API URLs to production
  * Test image uploads / JWT
  * Build signed APK / IPA

---

### **Step 3: Optional Features (Post-MVP)**

* Volunteer certificates
* Ratings & feedback
* Location-based matching
* Messaging
* Donation feature (after trust is built)

---

# 📝 Summary Table: Correct Development Order

| Phase      | Step | Description                                          |
| ---------- | ---- | ---------------------------------------------------- |
| Backend    | 1    | Create DB & tables (done)                            |
| Backend    | 2    | Pydantic Schemas                                     |
| Backend    | 3    | Repositories (CRUD)                                  |
| Backend    | 4    | Services (Business logic)                            |
| Backend    | 5    | Authentication & Role-based Authorization            |
| Backend    | 6    | Routers / API Endpoints                              |
| Backend    | 7    | File/Image Upload                                    |
| Backend    | 8    | Backend Testing                                      |
| Frontend   | 1    | Flutter Project Setup                                |
| Frontend   | 2    | API Integration                                      |
| Frontend   | 3    | UI Implementation                                    |
| Frontend   | 4    | State Management                                     |
| Frontend   | 5    | Local Storage (JWT, caching)                         |
| Frontend   | 6    | Frontend Testing                                     |
| Deployment | 1    | Backend Deployment                                   |
| Deployment | 2    | Frontend Deployment                                  |
| Optional   | 3    | Post-MVP features (certificates, ratings, messaging) |

---

✅ Following this **exact order ensures nothing breaks**
✅ You can iterate frontend & backend together after APIs are stable
✅ You can add more organizations types, optional images, badges later

---

If you want, I can **make a visual flow diagram** of this development order — like a roadmap — that shows **backend → frontend → deployment** so you can follow it easily.

Do you want me to do that?
