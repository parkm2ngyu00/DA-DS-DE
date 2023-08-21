use my_testdb;

# 1. 다양한 그룹 함수의 종류

# sum, avg, max, min
# stddev, variance (표준편차, 분산)

# 2. 특정 기준으로 그룸화한 후 그룹 함수 사용하기
# group by 함수
select deptno, sum(pay), max(pay), min(pay)
from professor
group by deptno;

select deptno, position, sum(pay), max(pay), min(pay)
from professor
where year(hiredate) > 1990
group by deptno, position;

select deptno, count(deptno), sum(pay), max(pay), min(pay)
from professor
group by deptno
having count(deptno) >= 2;
# 그룹 함수를 조건으로 사용하려면 where 대신 having을 사용해야 함

# 3. 소계와 전체 합계 구하기
select deptno, sum(pay), max(pay), min(pay)
from professor
group by deptno
with rollup;

select deptno, position, count(deptno), sum(pay), max(pay), min(pay)
from professor
where deptno in(101, 102, 103)
group by deptno, position
with rollup;

# 4. if 함수와 그룹 함수를 활용한 데이터 집계

# 5. 순위 값을 출력하기
select ename, sal, rank() over (order by sal desc) "급여순위"
from emp3;

select ename, sal, dense_rank() over (order by sal desc) "급여순위"
from emp3;

select *
from (select ename, sal, dense_rank() over (order by sal desc) as "급여순위"
from emp3) 순위
where 순위.급여순위 = 5;

select empno, ename, sal, deptno,
dense_rank() over (partition by deptno order by sal desc) "급여순위"
from emp3;

#6. 누적 합계 구하기
select empno, ename, sal, sum(sal) over(order by sal) "급여 누적합계"
from emp3;

select empno, ename, deptno, sal,
sum(sal) over(partition by deptno order by sal) "급여 누적합계"
from emp3;