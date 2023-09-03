def is_leap(year):
    # If year is dividable by 100 you can divide by 100 and check divisibility by 4 only
    year= year/100 if year%100==0 else year 
    return True if year%4==0 else False

year = int(input())
print(is_leap(year))