

"""
TABLE EMPLOYEE
id	name	department	salary
1	Arun	IT	60000
2	Ravi	IT	80000
3	Priya	HR	50000
4	Kumar	HR	70000
5	Meena	IT	90000
6	Sita	Sales	55000
7	John	Sales	75000
"""

''' PARTITION BY'''

#PARTITION BY keeps the rows but creates groups for calculations.

query = """
        SELECT name, department, salary,  AVG(salary) OVER (PARTITION BY department) AS dept_avg
        FROM EMPLOYEE;
        """


''' GROUP BY'''
# GROUP BY = Put rows into groups so that you can calculate something about each group.
query = """
        SELECT department , COUNT(*) FROM EMPLOYEE
        GROUP BY department
        """


''' ORDER BY '''

# ORDER BY = Arrange the rows By ASCENDING OR DESCENDING


query = """
        SELECT * FROM EMPLOYEE
        ORDER BY salary DESC; 
        ORDER BY salary ASC;
        """


# What does ; mean?
# The semicolon means:

# "This SQL statement is finished."


''' HAVING '''

# HAVING is used to filter groups created by GROUP BY.

query = """
        SELECT
        department,
        COUNT(*) AS employee_count
        FROM employees
        GROUP BY department;

        this is group by""" 

query = """
        SELECT
        department,
        COUNT(*) AS employee_count
        FROM employees
        GROUP BY department
        HAVING COUNT(*) > 2;
    
        """




# Remove the all the duplicate records but leave the first item:

query = """
        DELETE FROM EMP   
        WHERE id IN (
            SELECT id FROM (
                    SELECT id , ROW_NUMBER() OVER (
                            PARTITION BY name ORDER BY id
                            ) AS rn

                        FROM EMP
                      ) dp
                WHERE rn > 1

        """ 

''' ROAD MAP'''

"""
SELECT
  ↓
WHERE
  ↓
ORDER BY
  ↓
GROUP BY
  ↓
HAVING
  ↓
JOIN
  ↓
Subqueries
  ↓
Window Functions
  ↓
PARTITION BY
  ↓
ROW_NUMBER / RANK / DENSE_RANK
  ↓
CTE
  ↓
Real-world SQL problems

"""