drop database if exists hospital;
create database hospital;
use hospital;
--1
drop table if exists permission;
create table permission(
    per_id varchar(10) NOT NULL,
    per_name varchar(30) NOT NULL,
    Primary key(per_id)
);
--2
drop table if exists users;
create table users(
    id varchar(10) NOT NULL,
    first_name varchar(15) NOT NULL,
    middle_name varchar(15) ,
    last_name varchar(15) NOT NULL,
    gender char(1) NOT NULL,
    dob datetime NOT NULL,
    per_id varchar(10) NOT NULL,
    emailID varchar(30) NOT NULL,
    Primary key(id),
    FOREIGN KEY (per_id) references permission(per_id) ON UPDATE  CASCADE ON DELETE CASCADE,
    CONSTRAINT agender CHECK(gender='M' OR gender='F' or gender = 'T'),
    CONSTRAINT aemailID CHECK(emailID LIKE '%@%.%')
);
--3
drop table if exists admin;
create table admin(
    id varchar(10),
    first_name varchar(15) NOT NULL,
    middle_name varchar(15) ,
    last_name varchar(15) NOT NULL,
    login varchar(15) NOT NULL,
    password varchar(16) NOT NULL,
    Primary key(id)
);
--4
drop table if exists controls;
create table controls(
admin_id varchar(10),
users_id varchar(10),
Primary key(users_id,admin_id),
FOREIGN key (users_id) references users(id) ON UPDATE CASCADE on DELETE CASCADE,
FOREIGN KEY (admin_id) references admin(id) ON UPDATE CASCADE ON DELETE CASCADE
);
--5
drop table if exists tel_no_users;
create table tel_no_users(
users_id varchar(10) NOT NULL,
tel_no bigint(12) NOT NULL,
Primary key(users_id,tel_no),
FOREIGN key (users_id) references users(id) ON UPDATE CASCADE on DELETE CASCADE,
CONSTRAINT dtel_no  CHECK (LENGTH(tel_no)=10 AND tel_no NOT LIKE '%[^0-9%')
);
--6
drop table if exists address_users;
create table address_users(
users_id varchar(10) NOT NULL,
address varchar(100) NOT NULL,
Primary key(users_id,address),
FOREIGN key (users_id) references users(id) ON UPDATE CASCADE on DELETE CASCADE
);
--7
drop table if exists department;
create table department(
dep_id varchar(10) NOT NULL,
dep_name varchar(15) NOT NULL,
Primary KEY(dep_id)
);
--8
drop table if exists doctor;
create table doctor(
doc_id varchar(10) NOT NULL,
doc_ssn varchar(15) NOT NULL,
dep_id varchar(10) NOT NULL,
salary decimal(10,2) NOT NULL,
Primary key(doc_id),
FOREIGN KEY (doc_id) references users(id) ON UPDATE CASCADE on DELETE CASCADE,
FOREIGN KEY (dep_id) references department(dep_id) ON UPDATE CASCADE ON DELETE CASCADE, 
Unique key(doc_ssn),
CONSTRAINT gsalary CHECK(salary>0)
);
-- 9
drop table if exists maintenanceSchedule;
create table maintenanceSchedule(
dep_id varchar(10) NOT NULL,
costPerWeek int NOT NULL,
timeOfUnaivailbility int ,
Primary key(dep_id),
FOREIGN KEY (dep_id) references department(dep_id) ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT hcostPerWeek CHECK(costPerWeek>0)
);
--10
drop table if exists treatment;
create table treatment(
t_id varchar(10) NOT NULL,
t_name varchar(30) NOT NULL,
Primary key(t_id)
);
--11
drop table if exists medicine;
create table medicine(
m_id varchar(10) NOT NULL,
m_name varchar(30) NOT NULL,
mrp decimal(8,2) NOT NULL,
discount decimal(4,1) NOT NULL,
Primary key(m_id),
CONSTRAINT jmrp CHECK(mrp>0),
CONSTRAINT jdiscount CHECK(discount>=0)
);
--12
drop table if exists dosage;
create table dosage(
m_id varchar(10) NOT NULL,
med_salt varchar(15) NOT NULL,
med_availibilty varchar(15) NOT NULL,
Primary key(m_id),
FOREIGN KEY (m_id) references medicine(m_id) ON UPDATE CASCADE on DELETE CASCADE
);
--13
drop table if exists patient;
create table patient(
p_id varchar(10) NOT NULL,
adm_date datetime NOT NULL,
complaints varchar(100) ,
Primary key(p_id),
FOREIGN KEY(p_id) references users(id) ON UPDATE CASCADE on DELETE CASCADE
);
--14
drop table if exists medicalRecord;
create table medicalRecord(
p_id varchar(10) NOT NULL,
doc_id varchar(10) NOT NULL,
m_id varchar(10) NOT NULL,
t_id varchar(10) NOT NULL,
disease varchar(15),
Primary KEY(p_id,doc_id,m_id),
FOREIGN KEY (p_id) references patient(p_id) ON UPDATE CASCADE on DELETE CASCADE,
FOREIGN KEY (doc_id) references doctor(doc_id) ON UPDATE CASCADE on DELETE CASCADE,
FOREIGN KEY (m_id) references medicine(m_id) ON UPDATE CASCADE on DELETE CASCADE,
FOREIGN KEY (t_id) references treatment(t_id) ON UPDATE CASCADE on DELETE CASCADE
);
--15
drop table if exists other_workers;
create table other_workers(
w_id varchar(10) NOT NULL,
job varchar(10) NOT NULL,
salary decimal(8,2) NOT NULL,
FOREIGN KEY(w_id) references users(id) ON UPDATE CASCADE on DELETE CASCADE
);
--16
drop table if exists grade_1;
create table grade_1(
worker_id varchar(10) NOT NULL,
equipments_used varchar(30) ,
FOREIGN KEY(worker_id) references other_workers(w_id) ON UPDATE CASCADE ON DELETE CASCADE
);
--17
drop table if exists grade_2;
create table grade_2(
worker_id varchar(10) NOT NULL,
hours int  ,
contractor_name varchar(30) NOT NULL,
FOREIGN KEY(worker_id) references other_workers(w_id) ON UPDATE CASCADE ON DELETE CASCADE
);
