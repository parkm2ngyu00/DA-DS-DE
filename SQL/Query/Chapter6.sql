use my_testdb;

# 1. 등가 조인
select e.ename "사원이름", d.dname "부서이름"
from emp3 e, dept3 d
where  e.deptno = d.deptno;

select s.name, d.dname, p.name
from student s, department d, professor p
where s.deptno1 = d.deptno
and s.profno = p.profno;

select s.name, p.name
from student s, professor p
where s.profno = p.profno
and s.deptno1 = 101;

# 2. 비등가 조인
select c.gname "고객이름", g.gname "상품이름"
from customer c, gift g
where c.point between g.g_start and g.g_end;

# 3. outer join
select s.name "학생이름", p.name "지도교수이름"
from student s left outer join professor p
on s.profno = p.profno;
# outer join은 성능이 나쁘기 때문에 사용하지 않는것이 좋다

# 4. self join
select a.empno "사원번호", a.ename "사원이름",
a.mgr "상사의 사원번호", b.ename "상사이름"
from emp3 a, emp3 b
where a.mgr = b.empno;

# 5. join을 활용한 intersect(교집합)/minus(차집합) 구현하기

# 6. update에 join 활용하기