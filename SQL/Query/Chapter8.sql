# 제약조건의 이해와 활용
use my_testdb;

create table dept4(
deptno int primary key,
dname varchar(10) not null,
loc varchar(10) not null);

insert into dept4 values(10, '총무부', '3F');
insert into dept4 values(20, '생산부', '1F');
insert into dept4 values(30, '영업부', '2F');

select * from dept4;

create table emp4 (
empno int primary key,
ename varchar(10) not null,
deptno int,
foreign key (deptno) references dept4(deptno));

insert into emp4 values(1001, '서진수', 10);
insert into emp4 values(1002, '일지매', 20);
insert into emp4 values(1003, '전우치', '30'); # 이렇게 써도 자체적으로 int형으로 바꿔주지만, 이렇게 쓰지 않는것이 좋다.

select * from emp4;

# 기존 테이블에 제약 조건 추가하기
alter table dept5 add primary key(deptno);

alter table emp5 add constraint foreign key(deptno)
references dept5(deptno) on delete set null;
# dept5 테이블의 deptno를 참조하는 emp 테이블의 deptno인 조건을 추가한다.
# 만약 부모 테이블의 데이터가 삭제되면 자녀 테이블의 해당 외래키를 null값으로 만든다.

# 제약조건 확인 및 삭제하기
select * from information_schema.table_constraints
where table_name = 'emp4';

# 삭제하는 문법
# ALTER TABLE 테이블명 DROP KEY 제약조건이름 ;
