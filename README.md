The provided instructions outline the process of setting up a Django web framework to enable Internationalized Domain Name (IDN) compliant websites.

### Below is a step-by-step guide to set up a Django web framework for IDN compliant websites:
### First, ensure you have Python and pip installed on your system.
### Create a virtual environment for running the Django code. 
### Open a terminal or command prompt and Run the following command to create a virtual environment named 'env':
### python -m venv env
### Activate the virtual environment
### On Windows activate it by .\env\Scripts\activate
### On macOS/Linux activate it by command source env/bin/activate
### Download the code from the git repository. Replace repository_url with the actual URL of the repository.
### git clone repository_url
### cd repository_directory
### Install the required packages from the requirements.txt file using pip:
### pip install -r requirements.txt
### Open the hosts file on your local desktop/laptop machine using any text editor (e.g., Notepad on Windows, TextEdit on macOS, or any text editor on Linux).
### Add the following settings to the hosts file:
### 127.0.0.1 example.com
### 127.0.0.1 उदाहरण.भारत
### Add additional IDN domains as needed
### Save the hosts file.
### Run the Django code using the manage.py utility:
### python manage.py runserver 80
### access yor application with domain example.com or उदाहरण.भारत in browser URL .
### Now, your Django application should be running locally and accessible through the specified IDN domains. Make sure to replace example.com and उदाहरण.भारत with your actual domain names. Additionally, ensure that your Django application is configured to handle IDN  domains correctly.
### For more information on making your website IDN ready, refer to this link [click here](https://bhashanet.in/sop_document_page).
![Screenshot_4-4-2024_143534_xn----5td2fbm4cid4fzbcd3q xn--h2brj9c](https://github.com/bhashanet/django_idn_compliant_code/assets/165909590/f64d5622-4a48-447c-a0ea-29bc07ea8d83)
