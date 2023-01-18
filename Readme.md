**Install**

requirements.txt after creating a virtual env.

**Configure host names**

Now, we need to map the hostnames to the local machine.

* **_For Linux users,_** 

navigate to the /etc/hosts

* **_For Windows users,_** 

follow the path C:\Windows\System32\Drivers\etc\.

Open the host file using notepad or any other text editor and add our hosts as shown below:

`127.0.0.1 school.local

127.0.0.1 nairobi.school.com`

similarly for other databases add the hostnames.

**Test**

Now, we can run the local server and test our multitenant sites:

`python manage.py runserver school.local:8000
`
When the local host starts the server, you can access the tenant sites using the following URLs:


**Tenant Default:**

    Main site - http://school.local:8000/
    Admin site - http://school.local:8000/admin/

**Tenant Nairobi:**

    Main site - http://nairobi.school.com:8000/
    Admin site - http://nairobi.school.com:8000/admin

