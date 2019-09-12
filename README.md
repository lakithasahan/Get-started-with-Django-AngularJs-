# Get-started-with-Django-AngularJs
 This is a simple site designed incoperating angularjs and django. Basically in this example i will be discussing about the main functions in angular that going to be extreamly usefule.


AngularJS is a JavaScript framework. It can be added to an HTML page with a <script> tag.                 
AngularJS extends HTML attributes with Directives, and binds data to HTML with Expressions.

## AngularJS extends HTML with ng-directives.                                                                                               
The **ng-app** directive defines an AngularJS application.                                                                                     
The **ng-model** directive binds the value of HTML controls (input, select, textarea) to application data.                                           
The **ng-bind** directive binds application data to the HTML view.                                                                              


### Code
```html 
<!DOCTYPE html>
<html>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
<body>

<div ng-app="">
  <p>Name: <input type="text" ng-model="message"></p>
  <p ng-bind="message"></p>
</div>

</body>
</html>
```

### Explanation about the above exmaple code
AngularJS starts automatically when the web page has loaded.                                                                                        


The **ng-app** directive tells AngularJS that the ```html<div>``` element is the "owner" of an AngularJS application                 
The **ng-model** directive binds the value of the input field to the application variable *message*                                          
The **ng-bind** directive binds the content of the ```html<p>``` element to the application variable *message*   



### AngularJS Applications

AngularJS **modules** define AngularJS applications.                                                                                    
AngularJS **controllers** control AngularJS applications.                                                                                     
The **ng-app** directive defines the application, the **ng-controller** directive defines the controller.                                     


### Example code for introduction of Angular js **modules** and **controllers** 


#### This HTML code should be in your index.html file in django template folder

```html 

{% load staticfiles %}
{% load static %}

<!DOCTYPE html>
<html>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
<script type="text/javascript" src="{% static 'main.js' %}"></script>
<body>
{% verbatim %} 
<div ng-app="myApp" ng-controller="myCtrl">

First Name: <input type="text" ng-model="firstName"><br>
Last Name: <input type="text" ng-model="lastName"><br>
<br>
Full Name: {{firstName + " " + lastName}}

</div>
{% endverbatim %}
 </body>
</html>
```
### Important factors to remember

1)Since Django and Angular both use **{{}}** tags to avoid confusion, when we want to use **{{}}** in Angular framework we have to add **{% verbatim %} {% endverbatim %}** surounding the ng-app as shown above.                                                                               
2)Don't forget to **load** and add the path of your static directory where you store main.js file to your Django settings file as above.                                       
```
STATIC_URL = '/static/'
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'node_modules/angular'),
)
```
#### Below Javascript file hould be in your static folder,Always remeber to give the correct script path location in index.html file
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
