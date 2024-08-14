CREATE TABLE receitas (
    id SERIAL PRIMARY KEY,
    receita VARCHAR(255),
    pa_exerc VARCHAR(255),
    dt_vcto DATE,
    vl_original NUMERIC,
    sdo_devedor NUMERIC,
    situacao VARCHAR(255)
);
