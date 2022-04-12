Class rccpy.AoC20 {
/// docker-compose exec iris iris session iris "##class(rccpy.AoC20).Run()"
ClassMethod Run()
{
	write #!,"Welcome to embedded Python Demo"
			,!,"select day as described on https://adventofcode.com/"
			,!,"day 0 to exit",!
	set day=0
	for {
		write !?5,"day (1..25) ["_$i(day)_"]:" read d,! 
		if d'="" quit:'d  set day=d
		if (day<1)||(day>25) write ?5,"    Ooops",! set day=0 continue
		do ..py(day)
		if day=25 set day=0
	}
	write !,"good bye",!
	quit
}

ClassMethod py(day = "") [ Private ]
{
	quit:'day 0
	write !,"+++++ starting : day"_day_" +++++++++",! 
	set module="d"_$e(100+day,2,3)
		,py=##class(%SYS.Python).Import(module)
		,a=py.SetStdIOMode(1)
	if a    ; just for Code SMELL
part		
	read !?5,"select part (1,2,*=all,0=skip) [*] :",part#1,!
	if part="" set part="*"
	if '$lf($lb(1,2,"*",0),part) {
		write ?10,"1 2 * 0 only !!!"
		goto part
		}
	do $case(part,	0:0,
					1:1,
					2:2,
					:3)
	if part goto part
	quit 
3	do 1,2	
0	write !,"+++++++++ done : day"_day_" +++++++++",!
	quit
1	set ans=py.p1()
	write !?5,"part 1: ",ans,!
	quit
2	set ans=py.p2()
	write !?5,"part 2: ",ans,!
	quit
}

}
