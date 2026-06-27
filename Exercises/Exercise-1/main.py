import requests
import os
import zipfile
download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]



def main():
    # your code here
    #create the directory downloads if it doesn't exist
    os.makedirs("downloads", exist_ok=True)
    #download the files one by one.
    for uri in download_uris:
        
        data = requests.get(uri)
        
        if data.status_code == 200 :
        
            tgt_path = os.path.join("downloads", uri.split('/')[-1])
            
            with open(tgt_path, "wb") as f:
                f.write(data.content)
            
            with zipfile.ZipFile(tgt_path, 'r') as zip_ref:
                zip_ref.extractall("downloads")
            
            os.remove(tgt_path)
        
        else:
            print("Failed to fetch file from: " + uri)
            
    



if __name__ == "__main__":
    main()
