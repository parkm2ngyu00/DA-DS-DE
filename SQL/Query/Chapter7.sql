# 1. 새로운 칼럼 생성하기
alter table temp5
add column tel varchar(50) default '111-222-3333';

# 2. 칼럼의 크기 조정하기
alter table temp_5
modify column tel varchar(50);

# 3. 칼럼 이름 변경하기
alter table temp_5
change column tel phone varchar(40);

# 4. 칼럼 삭제하기
alter table temp_5
drop column phone;

# 5. 테이블 이름 변경하기
alter table temp_5 rename temp_7;

# truncate/drop - 삭제하기
# truncate : Data 부분 삭제
# drop : Table 자체를 삭제
truncate table temp_4;
drop table temp_4;

# 주요 DML 명령어 사용하기
create table temp_8 (
no int default 9999,
name varchar(10) default 'aaa',
birth datetime default current_timestamp);

insert into temp_8(no, name, birth)
values(1, '박민규', '2000-10-26');

insert into temp_8
values(2, '홍길동', '1999-11-17');

create table temp_9
as
select * from emp3
where 1=2;
# 데이터가 0건인 상태로 저장

insert into temp_9
select * from emp3
where sal <= 1500;

select * from temp_9;

# update
update temp_9 set sal = sal * 3
where sal <= 1000;

select * from temp_9;

# delete - 특정한 행을 삭제하기 위한 명령어
select * from temp_9
order by hiredate;

delete from temp_9
where hiredate > '1982-01-01';

select * from temp_9
order by hiredate;

# merge - 데이터 합치기
insert into p_total(pno, name, price)
select pno, name, price
from p_01
on duplicate key update
pno = p_01.pno,
name = p_01.name,
price = p_01.price;

# 트랜잭션 관리하기
create table temp_10
as
select * from emp3
where sal <= 1500;

set autocommit = 0; # autocommit = 0으로 설정하면 commit이나 rollback명령을 수행해 트랜잭션을 확정시켜야 한다.

select * from temp_10;

start transaction;
update temp_10
set sal = sal * 1.5;

rollback; # 트랜잭션 안에서 수행했던 작업 취소

start transaction;
update temp_10 set sal = sal * 1.5;
delete from temp_10 where comm is null;
create table temp_11 (no int); # DDL 문장은 자동으로 commit, 따라서 rollback을 해도 이 이후의 명령들만 취소가 된다.
update temp_10 set comm = 200;
rollback;