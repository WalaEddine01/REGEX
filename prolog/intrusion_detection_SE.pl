
failed_logins(ip1, 6).
failed_logins(ip2, 2).

sql_attempt(ip3, "UNION SELECT * FROM users").
sql_attempt(ip4, "normal request").

data_transfer(ip5, 15).
data_transfer(ip6, 1). 

unauthorized_access(ip7, "/admin").
unauthorized_access(ip8, "/home").

brute_force_attack(IP) :-
    failed_logins(IP, Attempts),
    Attempts > 5,
    write(IP), write(' flagged for Brute Force Attack!'), nl.

sql_injection_detected(IP) :-
    sql_attempt(IP, Query),
    sub_string(Query, _, _, _, "SELECT"),
    write(IP), write(' flagged for SQL Injection Attempt!'), nl.

data_exfiltration_detected(IP) :-
    data_transfer(IP, Size),
    Size > 10,
    write(IP), write(' flagged for Data Exfiltration!'), nl.

unauthorized_admin_access(IP) :-
    unauthorized_access(IP, "/admin"),
    write(IP), write(' flagged for Unauthorized Admin Access!'), nl.

