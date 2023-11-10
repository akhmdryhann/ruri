FROM python:3.11
WORKDIR /app
#Installing Python packages through requirements.txt file
 RUN pip install -r requirements.txt
 RUN pip install pandas scikit-learn sklearn flask gunicorn
 
 # Copy the model's directory and server.py files
 ADD server.py server.py
 
 #Exposing port 5000 from the container
 EXPOSE 5000
 #Starting the Python application
 CMD ["111.py", "--bind", "0.0.0.0:5000", "server:app"]