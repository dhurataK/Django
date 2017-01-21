from django.shortcuts import render
from . import models
# Create your views here.
def index(req):

#FRIENDSHIPS FIRST PART
    #1. Filter all of the users such that we only get back users with the last_name of Rodriguez.
    # users = models.Users.objects.filter(last_name='Rodriguez')

    #2. Filter all of the users such that we have all of the users except people with the last_name Rodriguez.
    # users = models.Users.objects.exclude(last_name='Rodriguez')

    #3.Using filter, get all of the users with the last_name Rodriguez and all of the users with the first_name Daniel.
    # users = models.Users.objects.filter(last_name='Rodriguez') | models.Users.objects.filter(first_name='Daniel')

    #4.Get all of the Rodriguez except Madison
    # users = models.Users.objects.filter(last_name='Rodriguez') & models.Users.objects.exclude(first_name='Madison')

    #5.Get everyone except Daniel and Michael
    # myListOfTitles = ['Daniel ','Michael']
    # users = models.Users.objects.all() & models.Users.objects.exclude(first_name__in=myListOfTitles)

    #6.Have this users first_name and last_name print on the index.html.
    # users = models.Users.objects.get(id=1)

    #7.
    # users = models.Users.objects.get(last_name='Rodriguez')
    # In terminal it prints "MultipleObjectsReturned: get() returned more than one Users -- it returned 3!"

    #8.
    # users = models.Users.objects.get(id=10000)
    # DoesNotExist: Users matching query does not excist.

    #9. Order the users by first_name
    # users = models.Users.objects.order_by('-first_name')

    #10. Order the users by reverse last_name
    # users = models.Users.objects.order_by('-last_name').reverse()

    #11.Print all the Friendship objects in your terminal.
    # friendships = models.Friendships.objects.all()
    # for friend in friendships:
    #     print friend

    #12. You know how to get a single friend by the id (6), now retrieve the Friendships where the User at id 4 is the user in the friendships table!
    # user = models.Users.objects.get(id = 4)
    # print user.first_name
    # friendships = models.Friendships.objects.filter(user = user)
    # for friend in friendships:
    #     print friend

    #13. Retrieve the Friendships where the User at id 4 is the friend.
    # user = models.Users.objects.get(id = 4)
    # print user.id
    # friendships = models.Friendships.objects.filter(friend = user)
    # for friend in friendships:
    #     print friend.user.first_name

    #14. Retrieve the Friendships where the user is not user 4, 5, or 6.
    # exclude_users = models.Users.objects.filter(id__in = [4,5,6])
    # friendships = models.Friendships.objects.exclude(user__in=exclude_users)
    # friend = dict()
    # for f in friendships:
    #     if f.user not in exclude_users:
    #         friend[f.user.id] = f.user
    # print friend
    # print friendships

#FRIENDSHIPS PART 2
    #1.Starting with Friendships, show all of the user and friend first
    # and last names on your index.html page. You can loop through and
    # get the user.first_name directly on the index.html page, maybe something
    # like {{friendship.user.first_name}}
    # friend = models.Friendships.objects.all()
    # friend = models.Friendships.objects.filter(user__id=1)

    #2.Print all of the friends' first and last names associated with
    # user__first_name = 'Michael' on your index.html page.
    # friend = models.Friendships.objects.filter(user__first_name='Michael')
    # print friend.query

    #3. Print all of the friends' first names who Daniel is not friends with on your index.html page.
    # friend = models.Friendships.objects.exclude(user__first_name='Daniel')

    #4. Print all of the friends who are friends with both User with the id of 1
    # and with Users with the last name Hernandez.
    # friend = models.Friendships.objects.filter(user__id=1) | models.Friendships.objects.filter(user__last_name='Hernandez')

    #5.Order these by friend first_name and print them on your index.html page.
    # (Note the double output of Daniel Moore!). Try adding .distinct(),
    # and make sure to still print the query on your terminal. Which column is distinct?
    # friend = models.Friendships.objects.order_by('user__first_name').distinct()
    # friend = models.Users.objects.order_by('friend__first_name').distinct()
    # print friend.query
    # context = {'friendships':friend}
    #6. In your views.py, try the following query:
    # users = models.Users.objects.filter(usersfriend__friend__id=2)
    # print (users.query)

    #7. Given this query, on your HTML page, try to print out the first and last name of Users with the id 2. (Note: this is tricky, take it once piece at a time!)
    # users = models.Users.objects.filter(usersfriend__friend__id=2)
    # print (users.query)

    users = (models.Users.objects.filter(friendsfriend__user__id=1) | models.Users.objects.filter(friendsfriend__user__last_name='Hernandez')).order_by('first_name').distinct()
    print users
    print users.query

    context = {
        'users' : users
    }

    return render(req, "friendapp/index.html", context)
