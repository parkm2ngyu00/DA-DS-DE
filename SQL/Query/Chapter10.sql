use my_testdb;

create view vemp
as
select empno, ename, deptno
from emp3
where deptno in(10, 20);

drop view vemp;

select * from vemp;
