(function(){
	'use strict';

	angular.module('bookmela.home')
	.config(['$routeProvider', config])

	function config($routeProvider){
		$routeProvider
		.when('/',{
			templateUrl: '/static/html/home.html',
			// controller: 'ScrumboardController',
		})
		.when('/login',{
			templateUrl: '/static/html/login.html',
			// controller: 'LoginController',
		})
		.otherwise('/');
	}


})();