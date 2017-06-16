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


CREATE OR REPLACE VIEW sig_limite_centropoblado AS (
	SELECT	cp.id AS CODIGO,
			cp.nombre AS CP_NOMBRE,
			cp.distrito_id AS DIST_UBIGEO,
			cp.geom AS GEOM
	FROM ubigeo_centropoblado cp
);


CREATE OR REPLACE VIEW sig_catastro_sector AS (
	SELECT	sec.id AS CODIGO,
			sec.nombre AS SEC_NOMBRE,
			sec.centro_poblado_id AS CENTROPOBLADO,
			sec.geom AS GEOM
	FROM catastro_sector sec
);

CREATE OR REPLACE VIEW sig_catastro_manzana AS (
	SELECT	mzn.id AS ID,
			mzn.codigo AS CODIGO,
            mzn.letra  AS LETRA,
			mzn.sector_id AS SECTOR,
			mzn.geom AS GEOM
	FROM catastro_manzana mzn
);

CREATE OR REPLACE VIEW sig_catastro_lote AS (
	SELECT	lte.id AS ID,
			lte.codigo AS CODIGO,
			lte.manzana_id AS MANZANA,
			lte.geom AS GEOM
	FROM catastro_lote lte
);
