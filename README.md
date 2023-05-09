# Pixela Graphing API

A python program that utilizes the Pixela Graphing API to create a graph and add, update and delete data from the graph.

![Screenshot (18)](https://github.com/GokulBakkiyarasu/pixela-graphing-api/assets/87391223/564df53b-61b7-4a61-99a6-1fc1691adeb9)

## Features
- Create a user account
- Create a graph
- Add data to the graph
- Update data on the graph
- Delete data from the graph

## Getting Started
To get started with this program, clone the repository and open the file in your preferred code editor. Make sure you have the requests and datetime python libraries installed before running the program.

### Prerequisites
- Python 3.x
- requests
- datetime

### Installation
1. Clone the repository: 
   ```
   git clone https://github.com/your_username/pixela-graphing-api.git
   ```
2. Install dependencies:
   ```
   pip install requests
   ```
3. Run the program:
   ```
   python main.py
   ```

## Usage
1. Create a user account: Modify the `USERNAME` and `TOKEN` variables to your desired values and run the program. A user account will be created with the given username and token.
2. Create a graph: Modify the `graph_parameters` dictionary to your desired values and run the program. A graph will be created with the given parameters.
3. Add data to the graph: Modify the `pixel_parameters` dictionary with the date and quantity of data you want to add to the graph and run the program. Data will be added to the graph on the specified date.
4. Update data on the graph: Modify the `update_data` dictionary with the updated quantity of data you want to replace the existing data with and run the program. The quantity of data on the specified date will be updated with the new value.
5. Delete data from the graph: Run the program with the `delete()` function to delete the data on the specified date from the graph.

## File structure
```
├── main.py                    # Main program file
```

## Functions:
Creating a user account:
```python
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = post(url=API_ENDPOINT, json= pixela_parameters)
```

Creating a graph:
```python
graph_parameters = {
    "id": "graph2",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

response = post(url=graph_endpoint, json=graph_parameters, headers=header)
```

Adding data to the graph:
```python
today = datetime.now()
pixel_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs/graph2"
pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "30",
}

response = post(url=pixel_endpoint, json=pixel_parameters, headers=header)
```

Updating data on the graph:
```python
update_pixel_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs/graph2/{pixel_parameters['date']}"
update_data = {
    "quantity": "80"
}

response = put(url=update_pixel_endpoint, json=update_data, headers=header)
```

Deleting data from the graph:
```python
response = delete(url=update_pixel_endpoint, headers=header)
```
## Contributing
Contributions to this project are welcome. To contribute, follow these steps:
1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make and commit your changes (`git commit -am "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
