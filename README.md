# Scammer-takedown
A scambaiting tool for flooding a scammers database with false data. 

_**NOTE:**_ Using this script is only ment for people who know what there doing. By running the script you assume the risks and responsiblity if you target a ligitement business.

_**Note:**_ Project is still in beta, Don't expext it to have modularity without modding the code.

# Install

Type or copy the following into the terminal to install and run.

```git clone https://awdaw```
```cd scammer-takedown```
```python3 main.py```

# Usage

Before running, you need to configue the python script.

1. Inside the script there is a data variable, inside is a example for a password phishing form, however this can be adapted to support other types of forms.
2. In the data variable, replace the "passwd" with the name of the input, you can look for the name of the input using an inspector tool in your browser, once you find a form element look for the following

```<input name="this-is-a-name">```

3. with the name of the input tag, the formating for the data tag should look like;

``` 
data = {
    "name1": "value1",
    "name2": "value2"
}
```

## Optional usage

Scammer takedown is also packaged with a JSON file **With a ton** of names. Each variable is already declared and ready for use.
all you need to do is format your data variable to the following.

``` 
data = {
    "name1": "value1",
    "name2": "value2",
    "name3": fname,
    "name4": lname
}
```

## Understanding the response code


https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Support

If you want to support me and my work, I'd prefer you to donate to Mozzila, Tor project, and other organizations that provide for a safer internet.
