use my_testdb;

select * from emp;

desc emp;

select name from emp;

select name, 'is good~' from emp;

select concat(name, ' is good~')
from emp;

select name, birthday from emp;

select name "이름", pay "연봉" , pay*1.1 "인상연봉"
from emp;

select empno as "사원번호", name "사원명", birthday "생일"
from emp;

select deptno from emp;

select distinct deptno from emp;

select name, deptno, hobby
from emp
where deptno = 1011;

select name, hobby
from emp
where hobby = 'Climb';

select deptno, dname, build
from department
where deptno >= 100 and deptno <= 200;

select profno, name, deptno
from professor
where deptno in(101, 102, 103);

select name, pay
from emp
where name like 'K%';

select deptno, name, bonus
from emp2
where deptno in(1001, 1002, 1003, 1004)
and bonus is null;

select deptno, name, bonus
from emp2
where deptno = 1001
and bonus = 250;

select deptno, name, bonus
from emp2
where (deptno = 1000
or deptno = 1001)
and bonus >= 250;

select deptno, name, birthday
from emp
where deptno in(1000, 1001, 1002, 1003)
order by birthday;

select deptno, name, birthday
from emp
where deptno in(1000, 1001, 1002, 1003)
order by birthday desc;

select name, lower(name) "소문자", upper(name) "대문자"
from student
where deptno1 = 101;

select name, left(name, 1) "LEFT", right(name, 1) "RIGHT"
from student
where deptno1 = 101;

select left('홍길동', 1) "left", mid('올길동', 2, 1) 'mid',
		right('홍길동', 1) "right"
from dual;

select length('서진수') "바이트수", char_length('서진수') "글자수"
from dual;

select
substr('MySQL', 3) "결과1",
substr('MySQL', 3, 2) "결과2",
substring('MySQL', 3) "결과3"
from dual;

select
substring_index('blog.naver.com', '.', 1) "결과1",
substring_index('blog.naver.com', '.', 2) "결과2",
substring_index('blog.naver.com', '.', 3) "결과3",
substring_index('blog.naver.com', '.', -1) "결과4",
substring_index('blog.naver.com', '.', -2) "결과5"
from dual;

select
substring_index('blog.naver.com', '.', 1) "첫번째",
substring_index(substring_index('blog.naver.com', '.', 2), '.', -1) "가운데",
substring_index('blog.naver.com', '.', -1) "마지막"
from dual;

select
'박민규' as "name", instr("박민규", '민') "instr";
# 결과 : 2

select
name, locate('S', name) "S_LOCATE"
from student
where deptno1 = 201;

select name, hobby,
lpad(hobby, 15, '*') "LPAD",
rpad(hobby, 15, '*') "RPAD"
from emp
where deptno in(1001, 1002, 1003);

select rpad('홍길동', 10, '4567890') "RPAD";
# 홍길동4567890

# trim, ltrim, rtrim, replace --> 공백제거에 사용 가능한 함수들
select 
ltrim('   abc123   ') "LTRIM",
rtrim('   abc123   ') "RTRIM"
from dual;

select repeat('MySQL ', 3) "REPEAT"
from dual;

select '홍길동' as "원래이름", reverse('홍길동') "REVERSE"
from dual;

# 다양한 숫자 함수 사용하기
select avg(pay) "AVG", sum(pay) "SUM", max(pay) "MAX", min(pay) "MIN"
from professor
where deptno = 101;

# count
select name, bonus
from professor
where deptno = 101;

select count(name) "사용", count(bonus) "bonus"
from professor
where deptno = 101;

# ceil, floor
# div, mod (몫, 나머지)
# round, truncate, power (반올림, 버림, 제곱 수 출력하기)

# 다양한 날짜 관련 함수 사용하기

select current_date(), current_time(), current_timestamp()
from dual;

# datediff, period_diff (두 날짜 사이의 차이나는 일 수, 개월 수 출력)

# date_add (날짜에 주어진 값을 더하거나 뺀 값 출력)

# dayname, dayofmonth, dayofweek, dayofyear (주어진 날짜의 영문 이름과 일/주/연도에서 몇 번째 날짜인지를 출력함)

# last_day, makedate, maketime (있다고만 알아두자)

# week, weekday, month, year (속한 값 출력)

# 다양한 변환 함수 활용하기

# NULL 값을 다른 값으로 변환하기
select deptno, name, pay, bonus, concat(format((pay*12) + bonus, 1), '원') "연봉"
from professor
where deptno in(101, 102);

select deptno, name, pay, bonus,
ifnull(bonus, 0) "IFNULL", coalesce(bonus, 0) " COALESCE"
from professor
where deptno in(101, 102);

# 다양한 경우의 조건을 활용하기
# 문법 : if(조건, 참인경우 할 작업, 거짓인 경우 할 작업)
select profno, name, deptno,
if(deptno = '101', '컴퓨터공학과', '다른학과임') "학과명"
from professor
where deptno in(101, 102, 103);
# 2중 중첨 if문도 사용 가능

# case
select profno, name, deptno,
	case deptno
		when 101 then '컴퓨터공학과'
        when 102 then '전자공학과'
        when 103 then '기계공학과'
        else '학과번호를 확인하세요'
	end '학과명'
from professor
where deptno in(101, 102, 103);
