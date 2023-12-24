This repository contains a robust job portal built using Django, offering a comprehensive platform for both employers and job seekers. The portal facilitates job listings, applications, and connections between employers and potential candidates.

### Key Models

#### Employer

- **Attributes** : `company_name`, `company_address`, `company_description`, and more.
- **Description** : Represents an employer with details about their company and job offerings.

#### Job

- **Attributes** : `title`, `description`, `employer`, `posted_date`, `job_location`, `requirements`, etc.
- **Description** : Defines a job listing with specific details, associated with an employer.

#### JobSeeker

- **Attributes** : `name`, `email`, `contact_information`, `skills`, etc.
- **Description** : Represents an individual seeking job opportunities with their personal information and skillset.

#### JobApplication

- **Attributes** : `job`, `job_seeker`, `application_date`, `cover_letter`, `resume`, etc.
- **Description** : Facilitates the application process, linking jobs and job seekers, along with application materials.

### Features

- **User Authentication** : Utilizes Django's user model for authentication and authorization.
- **Job Listing and Applications** : Allows employers to post jobs and job seekers to apply with relevant details.
- **Document Upload** : Enables job seekers to upload resumes and additional documents for applications.
- **Association and Linkage** : Establishes relationships between employers, jobs, job seekers, and applications for seamless interactions.

Feel free to explore the codebase for an in-depth understanding of the implementation of these models within the Django framework. Contributions and feedback are welcome!
