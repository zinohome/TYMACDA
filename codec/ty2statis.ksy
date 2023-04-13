meta:
  id: ty2statis
  endian: be
seq:
  - id: msg_header_lineid
    type: u1
  - id: msg_header_traintype
    type: u1
  - id: msg_header_trainid
    type: u1
  - id: msg_header_date_year
    type: u1
  - id: msg_header_date_month
    type: u1
  - id: msg_header_date_day
    type: u1
  - id: msg_header_date_hour
    type: u1
  - id: msg_header_date_minute
    type: u1
  - id: msg_header_date_second
    type: u1
  - id: msg_header_date_msecond
    type: s2
  - id: dw_temp_min_out
    type: s2
  - id: dw_temp_max_out
    type: s2
  - id: dw_temp_ave_out
    type: s2
  - id: dw_temp_min_inn
    type: s2
  - id: dw_temp_max_inn
    type: s2
  - id: dw_temp_ave_inn
    type: s2
  - id: dw_optime_emerg_ivt
    type: u4
  - id: dw_oppdtime_emmerg_ivt
    type: u4
  - id: dw_opcount_emerg_ivt
    type: u4
  - id: dw_oppdcount_emerg_ivt
    type: u4
  - id: dw_optime_ef_u1
    type: u4
  - id: dw_optime_cf_u1
    type: u4
  - id: dw_optime_comp_u11
    type: u4
  - id: dw_optime_comp_u12
    type: u4
  - id: dw_optime_eh_u11
    type: u4
  - id: dw_optime_eh_u12
    type: u4
  - id: dw_oppdtime_ef_u1
    type: u4
  - id: dw_oppdtime_cf_u1
    type: u4
  - id: dw_oppdtime_comp_u11
    type: u4
  - id: dw_oppdtime_comp_u12
    type: u4
  - id: dw_opcount_cp_u11
    type: u4
  - id: dw_opcount_cp_u12
    type: u4
  - id: dw_opcount_eh_u11
    type: u4
  - id: dw_opcount_eh_u12
    type: u4
  - id: dw_opcount_fad_u1
    type: u4
  - id: dw_opcount_rad_u1
    type: u4
  - id: dw_oppdcount_ef_u1
    type: u4
  - id: dw_oppdcount_cp_u11
    type: u4
  - id: dw_oppdcount_cp_u12
    type: u4
  - id: dw_oppdcount_eh_u11
    type: u4
  - id: dw_oppdcount_eh_u12
    type: u4
  - id: dw_oppdcount_fad_u1
    type: u4
  - id: dw_oppdcount_rad_u1
    type: u4
  - id: dw_optime_ef_u2
    type: u4
  - id: dw_optime_cf_u2
    type: u4
  - id: dw_optime_comp_u21
    type: u4
  - id: dw_optime_comp_u22
    type: u4
  - id: dw_optime_eh_u21
    type: u4
  - id: dw_optime_eh_u22
    type: u4
  - id: dw_oppdtime_ef_u2
    type: u4
  - id: dw_oppdtime_cf_u2
    type: u4
  - id: dw_oppdtime_comp_u21
    type: u4
  - id: dw_oppdtime_comp_u22
    type: u4
  - id: dw_opcount_cp_u21
    type: u4
  - id: dw_opcount_cp_u22
    type: u4
  - id: dw_opcount_eh_u21
    type: u4
  - id: dw_opcount_eh_u22
    type: u4
  - id: dw_opcount_fad_u2
    type: u4
  - id: dw_opcount_rad_u2
    type: u4
  - id: dw_oppdcount_ef_u2
    type: u4
  - id: dw_oppdcount_cp_u21
    type: u4
  - id: dw_oppdcount_cp_u22
    type: u4
  - id: dw_oppdcount_eh_u21
    type: u4
  - id: dw_oppdcount_eh_u22
    type: u4
  - id: dw_oppdcount_fad_u2
    type: u4
  - id: dw_oppdcount_rad_u2
    type: u4
  - id: i_train_id
    type: u2
  - id: i_car_id
    type: u2
