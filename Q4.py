months = {"Jan":31,"Feb":28,"Mar":31,"Apr":30,"May":31,"Jun":30,"Jul":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}
month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
counter=0
maxcounter = 0
maxfirst = ""
first = ""
def repeat(date):
  new = ""
  for i in date:
    if i in new:
      return True
    new += i
  return False
for year in range(2026, 2098):
  for month_i in range(12):
    month_name = month_names[month_i]
    month_len = months[month_name]
    if month_name == "Feb" and year % 4 == 0:
      month_len += 1
    month_f = ("0" + str(month_i+1)) if month_i < 9 else str(month_i+1)
    for day in range(month_len):
      day_f = ("0" + str(day+1)) if day < 9 else str(day+1)
      date = f"{day_f}{month_f}{year-2000}"
      if repeat(date):
        counter+=1
        if counter > maxcounter:
          maxcounter = counter
          maxfirst = first
        if counter == 1:
          first = date
      else:
        if maxcounter == counter:
          last = date
        counter = 0

print(f"the first date in the answer is the day before {maxfirst}, the second date is  {last}, and it lasts for {maxcounter} days")
