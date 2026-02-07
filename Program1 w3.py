START

# Ask the user for the person's age
INPUT age

# Check the age and decide the category
IF age <= 1 THEN
    PRINT "Infant"
ELSE IF age < 13 THEN
    PRINT "Child"
ELSE IF age < 20 THEN
    PRINT "Teenager"
ELSE
    PRINT "Adult"
END IF

END

