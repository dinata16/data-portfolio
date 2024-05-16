-- Jumlah total New Covid19 tapi diurutkan berdasarkan jumlah kasus yang paling besar 
select Province, 
  max(Total_Cases) - max(Total_Deaths) - max(Total_Recovered) as Total_Active_Cases,
  max(Total_Cases) Total_Cases
from `sql_challenge_1.covid19`
where Province is not null
group by Province
order by 3 desc;


-- 2 iso code yang dgn total_kematian karena Covid19 sedikit
select 
  Location_ISO_Code,
  Location,
  max(Total_Deaths) Total_Deaths, 
  max(Total_Cases) Total_Cases_Min
from `sql_challenge_1.covid19`
where Location_ISO_Code != 'IDN'
group by 1,2
order by 4;

-- tangal ketika recovered_rate tinggi di Indonesia dan serta jumlah rate nya
select Date,
  Location, 
  Total_Cases, 
  Total_Deaths, 
  Total_Recovered, 
  Total_Active_Cases,
  Total_Recovered/Total_Cases*100 Case_Recovered_Rate
from `sql_challenge_1.covid19`
where Location_ISO_Code = 'IDN'
order by 1 desc;



-- total fatality rate dam recovered rate dari masing-masing isocode urutkan dari terendah
-- Case Fatality Rate
select Location_ISO_Code, 
  Location,
  (max(Total_Deaths)/max(Total_Cases))*100 Case_Fatality_Rate
from `sql_challenge_1.covid19`
where Location_ISO_Code != 'IDN'
group by Location_ISO_Code,Location
order by 3;

--Case Recovered Rate
select Location_ISO_Code, 
  Location,
  (max(Total_Recovered)/max(Total_Cases))*100 Case_Recovered_Rate
from `sql_challenge_1.covid19`
where Location_ISO_Code != 'IDN'
group by Location_ISO_Code,Location
order by 3;


-- tanngal ketika covid19 menyentuh 30000 (berdasarkan apa total case nya dari 30 atau kapan tanggal mulai 30, atau tanggal hanya ketika mau 30000)
-- Province 
select Date, Total_Cases, Location
from `sql_challenge_1.covid19`
where Total_Cases >= 30000 and Location_ISO_Code != 'IDN'
order by 1;

-- Country
select Date, Total_Cases
from `sql_challenge_1.covid19`
where Total_Cases >= 30000 and Location_ISO_Code = 'IDN'
order by 1;





-- Jumlah data when Covi19 >= 30.000
--Province
select count(Total_Cases) Jumlah_data
from `sql_challenge_1.covid19`
where Total_Cases >= 30000 and Location_ISO_Code != 'IDN';

--Country
select count(Total_Cases) Jumlah_data
from `sql_challenge_1.covid19`
where Total_Cases >= 30000 and Location_ISO_Code = 'IDN';