# Hospital-API-Django
A doctors consultation booking appointment django based project that allows patients book appointment for consultation.

# Features
- Registration and logging in of patients, doctors, pharmacists, lab technicians and nurses.
- Confirmation of Availability by Doctors.
- Patients can book doctors appointment.
- Connection to a pharmacist or lab technician.

# Usage
To run the project:
1. Clone the repository
2. Create a virtual environment. If you already have an existing virtual environment you can skip the creation step. Navigate to where the virtual environment is and activate the environment.
   ```bash
   python -m venv name_of_environment
   name_of_environment\Scripts\activate
   ```
3. Install requirements. 
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migration.
   ```bash
   python manage.py migrate
   ```
5. Run the application by starting the server
   ```bash
   python manage.py runserver
   ```
