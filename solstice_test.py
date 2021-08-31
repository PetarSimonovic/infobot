from pymeeus.Sun import Sun
from pymeeus.Epoch import Epoch

year = 2019  # datetime.datetime.now().year
target="winter"

# Get terrestrial time of given solstice for given year
solstice_epoch = Sun.get_equinox_solstice(year, target=target)

print("%s solstice for %d in Terrestrial Time is at:\n %s" %
      (target, year, solstice_epoch.get_full_date()))

print("%s solstice for %d in UTC, if last leap second was %s:\n %s" %
 (target, year, Epoch.get_last_leap_second()[:2], solstice_epoch.get_full_date(utc=True)))

solstice_local = (solstice_epoch + Epoch.utc2local()/(24*60*60))
print("%s solstice for %d in local time, if last leap second was %s\n"
 " and local time offset is %.2f hours:\n %s" %
 (target, year, Epoch.get_last_leap_second()[:2],
  Epoch.utc2local() / 3600., solstice_local.get_full_date(utc=True)))

