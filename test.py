from eos import *
from eos.item_filter import *
from api_handler import *





data_handler = JsonDataHandler('data/')  # Folder with Phobos data dump
cache_handler = JsonCacheHandler('data/cache/eos_tq.json.bz2')
SourceManager.add('tiamat', data_handler, cache_handler, make_default=True)

skill_groups = set(row['groupID'] for row in data_handler.get_evegroups() if row['categoryID'] == 16)
skills = set(row['typeID'] for row in data_handler.get_evetypes() if row['groupID'] in skill_groups)

fit = Fit()
fit.ship = Ship(32311)  # Navy Typhoon

skills = get_skills(keyId, verification_code, char)
add_skills_to_fit(fit, skills)

# 4x 800mm with hail
fit.modules.high.equip(ModuleHigh(2929, state=State.overload, charge=Charge(12779)))
fit.modules.high.equip(ModuleHigh(2929, state=State.overload, charge=Charge(12779)))
fit.modules.high.equip(ModuleHigh(2929, state=State.overload, charge=Charge(12779)))
fit.modules.high.equip(ModuleHigh(2929, state=State.overload, charge=Charge(12779)))
# 4x Torp launcher with nova rages
fit.modules.high.equip(ModuleHigh(2420, state=State.overload, charge=Charge(24519)))
fit.modules.high.equip(ModuleHigh(2420, state=State.overload, charge=Charge(24519)))
fit.modules.high.equip(ModuleHigh(2420, state=State.overload, charge=Charge(24519)))
fit.modules.high.equip(ModuleHigh(2420, state=State.overload, charge=Charge(24519)))

fit.modules.med.equip(ModuleMed(5945, state=State.overload))  # Top named 100MN MWD
fit.modules.med.equip(ModuleMed(4833, state=State.active, charge=Charge(32014)))  # Named med cap injector with 800
fit.modules.med.equip(ModuleMed(9622, state=State.active))  # Named EM hardener
fit.modules.med.equip(ModuleMed(5443, state=State.active))  # Best named scram
fit.modules.med.equip(ModuleMed(2281, state=State.active))  # T2 invuln

fit.modules.low.equip(ModuleLow(2048, state=State.online))   # T2 DC
fit.modules.low.equip(ModuleLow(519, state=State.online))    # T2 gyrostab
fit.modules.low.equip(ModuleLow(519, state=State.online))    # T2 gyrostab
fit.modules.low.equip(ModuleLow(22291, state=State.online))  # T2 BCU
fit.modules.low.equip(ModuleLow(22291, state=State.online))  # T2 BCU
fit.modules.low.equip(ModuleLow(4405, state=State.online))   # T2 DDA
fit.modules.low.equip(ModuleLow(4405, state=State.online))   # T2 DDA

fit.rigs.add(Rig(26082))  # T1 therm rig
fit.rigs.add(Rig(26088))  # T1 extender
fit.rigs.add(Rig(26088))  # T1 extender

# 8x Ogre II
fit.drones.add(Drone(2444, state=State.active))
fit.drones.add(Drone(2444, state=State.active))
fit.drones.add(Drone(2444, state=State.active))
fit.drones.add(Drone(2446, state=State.active))
fit.drones.add(Drone(2446, state=State.active))
fit.drones.add(Drone(2446, state=State.offline))
fit.drones.add(Drone(2446, state=State.offline))
fit.drones.add(Drone(2446, state=State.offline))

fit.implants.add(Implant(13231))  # 3% torp dmg
fit.implants.add(Implant(10228))  # 3% shield capacity
fit.implants.add(Implant(24663))  # zor hyperlink
fit.implants.add(Implant(13244))  # 3% turret dmg
fit.implants.add(Implant(13219))  # 3% large projectile dmg

fit.boosters.add(Booster(28672))  # Synth crash
fit.boosters.add(Booster(28674))  # Synth drop

try:
	fit.validate()
except ValidationError as error:
	print("failed")
	print(error.args[0])	
	print("failed")


print("dps, no reload: ", fit.stats.get_nominal_dps(reload=False).total)
print("dps, reload: ", fit.stats.get_nominal_dps(reload=True).total)