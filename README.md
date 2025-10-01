# Airflow DAG Project
  
### DAG Graph View

This screenshot shows the DAG graph in the Airflow UI. The three tasks are connected in sequence:
print_date → welcome_message → generate_random

<div>
<img src ="https://github.com/user-attachments/assets/45ae741e-1f92-423a-b7aa-413e16e31959" width = 300>

</div>

### Task Logs: Print Date (BashOperator)

The logs confirm that the date command ran successfully, showing the system’s current date and time.

<div>
<img src ="https://github.com/user-attachments/assets/68becfb9-8b52-4d97-9ddd-31f883b0d453" width = 300>

</div>

### Task Logs: Welcome Message (PythonOperator)

This task runs the Python function print_welcome() and outputs the custom welcome message:
<div>
<img src ="https://github.com/user-attachments/assets/ad539431-284c-4b34-89ff-d12603791c6a" width = 300>

</div>


### Task Logs: Generate Random (PythonOperator)

The logs show a random number generated (between 1–100). This number is written into the file /tmp/random.txt. Example log output:
<div>
<img src ="https://github.com/user-attachments/assets/0e337afb-fd16-47ed-b9b4-59739110164e" width = 300>

</div>

