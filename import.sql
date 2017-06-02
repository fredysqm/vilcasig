INSERT INTO vilcasig_dev.ubigeo_departamento SELECT codigo, nombre, geom, ST_CENTROID(geom), creado, modificado FROM vilcasig_old.ubigeo_departamento;
INSERT INTO vilcasig_dev.ubigeo_provincia SELECT codigo, nombre, geom, ST_CENTROID(geom), creado, modificado, departamento_id FROM vilcasig_old.ubigeo_provincia;
INSERT INTO vilcasig_dev.ubigeo_distrito SELECT codigo, nombre, geom, ST_CENTROID(geom), creado, modificado, provincia_id FROM vilcasig_old.ubigeo_distrito;
INSERT INTO vilcasig_dev.ubigeo_centropoblado SELECT cp.codigo, cp.nombre, p.geom, ST_CENTROID(p.geom), cp.creado, cp.modificado, cp.distrito_id
FROM vilcasig_old.ubigeo_centropoblado cp
INNER JOIN vilcasig_old.catastro_perimetro p ON (cp.codigo = p.centro_poblado_id)