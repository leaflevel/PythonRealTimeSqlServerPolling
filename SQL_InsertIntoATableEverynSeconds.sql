
use python
go

truncate table realtimelog

declare @i int = 0



WHILE @i < 100000000
	 begin 
	 set @i=@i+1
	 INSERT into realtimelog(random, datetime) 
	 values(cast(rand()* 1 as int), getdate()) 
	 WAITFOR DELAY '00:00:01:00' --Two seconds
	end
	 

select * from RealtimeLog


--alter table realtimelog
--alter column datetime datetime2

