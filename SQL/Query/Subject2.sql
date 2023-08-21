use my_testdb;

select * from emp;

# 150pg 1번
select deptno "부서번호", format(sum(pay), 0) "부서별 급여합계"
from emp
where deptno in(1001, 1002, 1003, 1004)
group by DEPTNO
order by sum(deptno);

# 과제2 (pg. 210)
create table customer4 (
no int primary key,
name varchar(30) default 'AAA',
tel varchar(15) default '1111',
email varchar(100) default 'abc@def.net');

desc customer4;

insert into customer4 values(2022001, '서진수', '02)111-2222', 'seojinsu@gmail.com');
insert into customer4 values(2022002, '손기동', '031)234-5678', 'skdong@daum.net');
insert into customer4 values(2022003, '정진교', '055)233-4678', 'jjk12345@naver.com');
insert into customer4 values(2022004, '홍길동', '054)4567-0987', 'hongkd1234@gmail.com');
insert into customer4 values(2022005, '일지매', '053)2233-4455', 'onejm2222@daum.net');

select * from customer4;

create table customer5
as
select name, tel
from customer4;

select * from customer5;

alter table customer5
add column birth varchar(20) default '9999-12-31';

select * from customer5;