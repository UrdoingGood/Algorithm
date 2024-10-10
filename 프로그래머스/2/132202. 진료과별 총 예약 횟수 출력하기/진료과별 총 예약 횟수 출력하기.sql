SELECT mcdp_cd AS '진료과코드', COUNT(*) AS "5월예약건수"
FROM appointment
WHERE apnt_ymd BETWEEN "2022-05-01" AND "2022-05-31"
    AND (apnt_cncl_yn != "Y" OR ~ISNULL(apnt_cncl_yn))
GROUP BY mcdp_cd
ORDER BY COUNT(pt_no) ASC, mcdp_cd ASC;


# SELECT * 
# FROM appointment;