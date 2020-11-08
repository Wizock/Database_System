registerQuery = self.connection.execute(
    '''
    INSERT INTO workers (firstName,lastName,email,userName,password,Age,Wage,position,employeeID) VALUES (?,?,?,?,?,?,?,?)
    ''',(register_lastName,register_email,register_userName,register_password,register_age,register_Wage,register_position,register_employeeID))