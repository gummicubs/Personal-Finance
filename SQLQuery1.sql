CREATE database Care;
GO

SELECT TOP 5 * 
FROM CanadaRealEstate;


SELECT COUNT(Address)
FROM CanadaRealEstate;
--There are 7,728 rows on homes for sale.

SELECT COUNT(DISTINCT Address)
FROM CanadaRealEstate;
--There are only 3,360 unique addresses.

SELECT *
FROM CanadaRealEstate
ORDER BY Address

SELECT COUNT(DISTINCT Place)
FROM CanadaRealEstate;
-- There are 308 neightborhoods.

SELECT COUNT(DISTINCT Website)
FROM CanadaRealEstate;
-- There  are 216 Real Estate Companies.

SELECT Place, AVG(Price) AS Average_Price, AVG(Sq_Ft) AS Average_Size, AVG(Beds) AS Averge_Bedrooms, AVG(Bath) AS Average_Bathrooms, COUNT(*) AS Num_of_Houses
FROM CanadaRealEstate
GROUP BY Place
ORDER BY Count(*) DESC