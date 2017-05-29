#vistas / capas

CREATE OR REPLACE VIEW sig_limite_departamento AS (
	SELECT CONCAT(codigo, '0000') AS UBIGEO,
			nombre AS DPTO_NOMBRE,
			geom AS GEOM
	FROM ubigeo_departamento
);


CREATE OR REPLACE VIEW sig_limite_provincia AS (
	SELECT CONCAT(p.codigo, '00') AS UBIGEO,
			d.nombre AS DPTO_NOMBRE,
			p.nombre AS PROV_NOMBRE,
			p.geom AS GEOM
	FROM ubigeo_provincia p
	INNER JOIN ubigeo_departamento d ON (p.departamento_id = d.codigo)
);


CREATE OR REPLACE VIEW sig_limite_distrito AS (
	SELECT	dt.codigo AS UBIGEO,
			d.nombre AS DPTO_NOMBRE,
			p.nombre AS PROV_NOMBRE,
            dt.nombre AS DIST_NOMBRE,
			dt.geom AS GEOM
	FROM ubigeo_distrito dt
    INNER JOIN ubigeo_provincia p ON (dt.provincia_id = p.codigo)
	INNER JOIN ubigeo_departamento d ON (p.departamento_id = d.codigo)
);


CREATE OR REPLACE VIEW sig_centropoblado_punto AS (
	SELECT	cp.id AS CODIGO,
			cp.nombre AS CP_NOMBRE,
			cp.distrito_id AS DIST_UBIGEO,
			cp._centroid AS GEOM
	FROM ubigeo_centropoblado cp
);


CREATE OR REPLACE VIEW sig_centropoblado_perimetro AS (
	SELECT	cp.id AS CODIGO,
			cp.nombre AS CP_NOMBRE,
			cp.distrito_id AS DIST_UBIGEO,
			cp.geom AS GEOM
	FROM ubigeo_centropoblado cp
);


