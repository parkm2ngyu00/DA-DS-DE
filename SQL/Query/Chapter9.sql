# 다양한 sub query의 이해와 활용
# pg.226

use my_testdb;

select empno, ename, sal
from emp3
where sal >
(select sal from emp3 where ename = 'ALLEN');

# sub query의 종류
# 1. 단일 행 sub query - sub query를 실행한 결과가 1건이 나오는 경우
select empno, ename, hiredate
from emp3
where hiredate > (
select hiredate
from emp3
where ename = 'FORD');

# 2. 다중 행 sub query

# in 연산자
select empno, ename, sal, deptno
from emp3
where sal in(
select sal
from emp3
where deptno = 10);
# >any 연산자
select empno, ename, sal, deptno
from emp3
where sal > any (
select sal
from emp3
where deptno = 10); # sal > 1300 와 동일
# <any 연산자
select empno, ename, sal, deptno
from emp3
where sal < any (
select sal
from emp3
where deptno = 10); # sal < 5000 와 동일
# <all 연산자
# 최소값 반환

# >all 연산자
# 최대값 반환

# 다중 칼럼 sub query
select ename, sal, deptno
from emp3
where (deptno, sal) in (select deptno, max(sal)
from emp3
group by deptno);

# 스칼라 서브 쿼리 (join과 역할 동일)

