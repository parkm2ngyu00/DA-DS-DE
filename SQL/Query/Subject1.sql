use my_testdb;

# 1번 문제
select profno "교수번호", name "교수이름", id "ID"
from professor
where left(id, 1) in('A', 'B', 'C', 'D', 'E', 'F', 'G');

# 2번 문제
select profno "교수번호", name "교수이름", deptno "학과번호"
from professor
where deptno = 101 or deptno = 102;

# 3번 문제
select profno "교수번호", name "교수이름", hpage "홈페이지주소"
from professor
where hpage is not null;

# 4번 문제
select profno "교수번호", name "교수이름", deptno "학과번호", bonus "BONUS"
from professor
where (deptno = 101 or deptno = 102)
and (bonus is not null);

# 5번 문제
select profno "번호", name "이름", deptno "학과번호"
from professor
where deptno = 101
union all
select studno, name, deptno1
from student
where deptno1 = 101;