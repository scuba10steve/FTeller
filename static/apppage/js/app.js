var app = angular.module('fteller-app', [])

app.controller('FtellerController', function($scope, $http)
{
    $scope.questions = []

    $scope.activeQuestion = ""

    $scope.lastQuestion = ""

    $scope.init = function() {
        console.log('getting questions...')

        $http({
            method: 'GET',
            url: '/questions',
        }).then(function(response) {
            questions = response.data
            pickQuestion()
        })

    }

    $scope.answerSingle = function() {

    }

    $scope.answer = function(answerval) {

        postdata = JSON.stringify({answer: answerval, questions: questions})
        $http({
            method: 'POST',
            data: postdata,
            url: "/answer"
        }).then(function(response) {
            console.log(response.data.valueOf())
        })
    }

    function pickQuestion() {

        var pattern = new RegExp('What is it?')

        for (var i = 0; i < questions.length; i++)
        {
            if (pattern.test(questions[i].value.valueOf()))
            {
                $scope.lastQuestion = questions[i]
                questions = questions.slice(questions.indexOf($scope.lastQuestion), 1)
                break
            }
        }
        x = Math.floor(Math.random() * questions.length)

        $scope.activeQuestion = questions[x].value.valueOf()
    }
})
