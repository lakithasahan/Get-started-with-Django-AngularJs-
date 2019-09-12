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









 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
