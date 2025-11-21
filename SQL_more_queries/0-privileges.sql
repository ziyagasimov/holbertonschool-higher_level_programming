#!/bin/bash

# Lists privileges for user_0d_1 and user_0d_2 on localhost
mysql -u root -p -e "
    SHOW GRANTS FOR 'user_0d_1'@'localhost';
    SHOW GRANTS FOR 'user_0d_2'@'localhost';
"
