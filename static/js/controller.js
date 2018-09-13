(function(){
		'use strict';

		angular
			.module('bookmela.home',['ngRoute'])

			.controller('HomeController',['$scope','$http','$location', HomeController]);

		function HomeController($scope,$http,$location){


			$scope.add=function(list, title){

		
		
					$location.url('/login')
				
			};



	}

	})();