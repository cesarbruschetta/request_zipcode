-- CEP 1 ----------------------------------------------------------------

SELECT
  log_logradouro.log_tipo_logradouro,
  log_logradouro.log_no as logradouro,
  log_bairro.bai_no as bairro,
  log_localidade.loc_no as cidade,
  log_localidade.ufe_sg as uf,
  log_logradouro.cep
FROM
   `log_logradouro`,`log_localidade`,`log_bairro`
WHERE
   log_logradouro.loc_nu_sequencial = log_localidade.loc_nu_sequencial
AND
   log_logradouro.bai_nu_sequencial_ini = log_bairro.bai_nu_sequencial
AND
   log_logradouro.cep = :CEP;

-- CEP 2 ----------------------------------------------------------------

SELECT
    Log_logradouro.LOC_NU_SEQUENCIAL,
    Log_logradouro.LOG_NOME AS LOGRADOURO,
    Log_logradouro.CEP,
    Log_logradouro.UFE_SG,
    Log_Logradouro.LOG_NU_SEQUENCIAL,
   Log_Logradouro.LOG_STATUS_TIPO_LOG,
    Log_bairro.BAI_NO AS INICIAL,
    Log_Localidade.LOC_NO,
        ( SELECT BAI_NO
          FROM LOG_BAIRRO
          WHERE BAI_NU_SEQUENCIAL = Log_Logradouro.BAI_NU_SEQUENCIAL_FIM) AS FINAL
FROM
    LOG_LOGRADOURO Log_logradouro,
    LOG_BAIRRO Log_bairro,
    LOG_LOCALIDADE Log_Localidade
WHERE
    (Log_logradouro.UFE_SG = Log_bairro.UFE_SG)
    AND (Log_logradouro.LOC_NU_SEQUENCIAL = Log_bairro.LOC_NU_SEQUENCIAL)
    AND (Log_logradouro.BAI_NU_SEQUENCIAL_INI = Log_bairro.BAI_NU_SEQUENCIAL)
    AND (Log_logradouro.UFE_SG = Log_localidade.UFE_SG)
    AND (Log_logradouro.LOC_NU_SEQUENCIAL = Log_localidade.LOC_NU_SEQUENCIAL)
    AND (Log_logradouro.CEP = :CEP)
ORDER BY
    Log_logradouro.LOG_TIPO_LOGRADOURO, Log_logradouro.LOG_NO


-- LOCALIDADE UF -------------------------------------------------------------

SELECT * FROM LOG_FAIXA_UF ORDER BY UFE_SG;

-- LOCALIDADE LOCALIDADE -------------------------------------------------------------

SELECT
    Log_localidade.LOC_NO,
    Log_localidade_Sub.LOC_NO AS LOC_SUB,
    Log_localidade.LOC_NU_SEQUENCIAL,
    Log_localidade.LOC_NU_SEQUENCIAL_SUB,
    Log_localidade.CEP,
    Log_localidade.UFE_SG,
    Log_localidade.LOC_IN_SITUACAO,
    Log_localidade.LOC_IN_TIPO_LOCALIDADE
FROM LOG_LOCALIDADE Log_localidade
    LEFT OUTER JOIN LOG_LOCALIDADE Log_localidade_Sub ON (Log_localidade.LOC_NU_SEQUENCIAL_SUB = Log_localidade_SUB.LOC_NU_SEQUENCIAL)
WHERE
    (Log_localidade.UFE_SG = :UFE_SG)
ORDER BY Log_localidade.LOC_NO

-- LOCALIDADE LOGRADOURO MATCH -------------------------------------------------------------

SELECT
  log_logradouro.log_tipo_logradouro,
  log_logradouro.log_no as logradouro,
  log_bairro.bai_no as bairro,
  log_localidade.loc_no as cidade,
  log_localidade.ufe_sg as uf,
  log_logradouro.cep
FROM
    log_logradouro, log_localidade, log_bairro
WHERE
    log_logradouro.loc_nu_sequencial = log_localidade.loc_nu_sequencial
AND
   log_logradouro.bai_nu_sequencial_ini = log_bairro.bai_nu_sequencial
AND
    log_logradouro.LOC_NU_SEQUENCIAL = :LOC_NU_SEQUENCIAL
AND
    MATCH (log_logradouro.LOG_NOME) AGAINST (:LOG_NOME IN BOOLEAN MODE);

-- LOCALIDADE LOGRADOURO LIKE -------------------------------------------------------------

SELECT
  log_logradouro.log_tipo_logradouro,
  log_logradouro.log_no as logradouro,
  log_bairro.bai_no as bairro,
  log_localidade.loc_no as cidade,
  log_localidade.ufe_sg as uf,
  log_logradouro.cep
FROM
    log_logradouro, log_localidade, log_bairro
WHERE
    log_logradouro.loc_nu_sequencial = log_localidade.loc_nu_sequencial
AND
   log_logradouro.bai_nu_sequencial_ini = log_bairro.bai_nu_sequencial
AND
    log_logradouro.LOC_NU_SEQUENCIAL = :LOC_NU_SEQUENCIAL
AND
    log_logradouro.LOG_NOME LIKE CONCAT('%', :LOG_NOME, '%');

-- UF ----------------------------------------------------------------

SELECT * FROM LOG_FAIXA_UF
ORDER BY UFE_SG;

-- LOCALIDADES ----------------------------------------------------------------

SELECT * FROM LOG_LOCALIDADE
WHERE
    LOG_LOCALIDADE.UFE_SG = UFE_SG
AND
    (LOG_LOCALIDADE.LOC_IN_SITUACAO = 1 OR LOG_LOCALIDADE.LOC_IN_SITUACAO = 2)
ORDER BY LOG_LOCALIDADE.LOC_NO;

-- BAIRROS ----------------------------------------------------------------

SELECT * FROM LOG_BAIRRO
WHERE
    LOG_BAIRRO.UFE_SG = UFE_SG
AND
    LOG_BAIRRO.LOC_NU_SEQUENCIAL = :LOC_NU_SEQUENCIAL
ORDER BY LOG_BAIRRO.BAI_NO;

-- BAIRROS CEP ----------------------------------------------------------------

SELECT L.LOG_NOME, L.CEP ,B.BAI_NO as Inicial,
    (
    SELECT BAI_NO
    FROM LOG_BAIRRO
    WHERE
    BAI_NU_SEQUENCIAL = L.BAI_NU_SEQUENCIAL_FIM
    ) as Final
FROM LOG_LOGRADOURO L, LOG_BAIRRO B
WHERE
    (L.BAI_NU_SEQUENCIAL_INI = B.BAI_NU_SEQUENCIAL)
    AND (L.UFE_SG                = :UFE_SG  )
    AND (L.LOC_NU_SEQUENCIAL     = :LOC_NU_SEQUENCIAL)
    AND (
        L.BAI_NU_SEQUENCIAL_INI = :BAI_NU_SEQUENCIAL
        OR
        L.BAI_NU_SEQUENCIAL_FIM = :BAI_NU_SEQUENCIAL
        )
ORDER BY L.LOG_NOME;