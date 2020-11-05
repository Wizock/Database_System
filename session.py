'''
this file is responsible for creating the session of the logged in user

this script will enable functions that correlate to the privledge and possitoin of a user

there are 3 main positions, 
    - worker
    - manager
    - admin

a worker can only login and begin thier shift which will set thier onJob status to thier Yes or No

a manager can see who is working and where and see how much they will make this shift, they may have just started
but the prejudice is that they will complete thier shift and calculate thier wage accordingly

the admin has the ability to create or delete reccords. 

--views--
worker:
    the worker can login and be asked to loggout inorder to begin his shift
    once the worker has logged in, their shift has begun for 5 seconds a peice but the time has been simplified to 5 seconds

manager:
    the manager can see what employee has logged in for a job
    the manager can see how much each employee can make
    the manager gets to see the tables in console

admin:
    the admin can type "delete" or "register" a worker
    the admin can also create managers
    
'''
