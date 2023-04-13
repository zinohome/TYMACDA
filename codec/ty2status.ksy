meta:
  id: ty2status
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
  - id: i_inner_temp
    type: s2
  - id: i_set_temp
    type: s2
  - id: w_passen_load
    type: u2
  - id: i_seat_temp
    type: s2
  - id: i_veh_temp
    type: s2
  - id: i_seat_hum
    type: s2
  - id: i_veh_hum
    type: s2
  - id: w_opmode_u1
    type: u2
  - id: i_fat_u1
    type: s2
  - id: i_rat_u1
    type: s2
  - id: i_dft_u11
    type: s2
  - id: i_dft_u12
    type: s2
  - id: i_sat_u11
    type: s2
  - id: i_sat_u12
    type: s2
  - id: i_suck_temp_u11
    type: s2
  - id: i_suck_pres_u11
    type: s2
  - id: i_sup_heat_u11
    type: u2
  - id: i_eev_pos_u11
    type: u2
  - id: i_suck_temp_u12
    type: s2
  - id: i_suck_pres_u12
    type: s2
  - id: i_sup_heat_u12
    type: u2
  - id: i_eev_pos_u12
    type: u2
  - id: w_opmode_u2
    type: u2
  - id: i_fat_u2
    type: s2
  - id: i_rat_u2
    type: s2
  - id: i_dft_u21
    type: s2
  - id: i_dft_u22
    type: s2
  - id: i_sat_u21
    type: s2
  - id: i_sat_u22
    type: s2
  - id: i_suck_temp_u21
    type: s2
  - id: i_suck_pres_u21
    type: s2
  - id: i_sup_heat_u21
    type: u2
  - id: i_eev_pos_u21
    type: u2
  - id: i_suck_temp_u22
    type: s2
  - id: i_suck_pres_u22
    type: s2
  - id: i_sup_heat_u22
    type: u2
  - id: i_eev_pos_u22
    type: u2
  - id: i_train_id
    type: s2
  - id: i_car_id
    type: s2
  - id: msg_reverse_3
    type: s2
  - id: msg_reverse_4
    type: s2
  - id: cfbk_eh_u22
    type: b1
  - id: cfbk_eh_u21
    type: b1
  - id: cfbk_eh_u12
    type: b1
  - id: cfbk_eh_u11
    type: b1
  - id: cfbk_comp_u22
    type: b1
  - id: cfbk_comp_u21
    type: b1
  - id: cfbk_comp_u12
    type: b1
  - id: cfbk_comp_u11
    type: b1
  - id: msg_reverse_5
    type: u1
  - id: b_cpflt_comp_u12
    type: b1
  - id: b_scflt_comp_u11
    type: b1
  - id: b_lpflt_comp_u11
    type: b1
  - id: b_cpflt_comp_u11
    type: b1
  - id: b_ocflt_cf_u12
    type: b1
  - id: b_ocflt_cf_u11
    type: b1
  - id: b_ocflt_ef_u12
    type: b1
  - id: b_ocflt_ef_u11
    type: b1
  - id: b_flt_rad_u1
    type: b1
  - id: b_flt_fad_u1
    type: b1
  - id: b_flt_eev_u12
    type: b1
  - id: b_flt_eev_u11
    type: b1
  - id: b_flt_eh_u12
    type: b1
  - id: b_flt_eh_u11
    type: b1
  - id: b_scflt_comp_u12
    type: b1
  - id: b_lpflt_comp_u12
    type: b1
  - id: b_flt_expboard_u1
    type: b1
  - id: b_flt_airclean_u1
    type: b1
  - id: b_flt_dftemp_u12
    type: b1
  - id: b_flt_dftemp_u11
    type: b1
  - id: b_flt_rnttemp_u1
    type: b1
  - id: b_flt_suplytemp_u12
    type: b1
  - id: b_flt_suplytemp_u11
    type: b1
  - id: b_flt_frstemp_u1
    type: b1
  - id: b_cpflt_comp_u22
    type: b1
  - id: b_scflt_comp_u21
    type: b1
  - id: b_lpflt_comp_u21
    type: b1
  - id: b_cpflt_comp_u21
    type: b1
  - id: b_ocflt_cf_u22
    type: b1
  - id: b_ocflt_cf_u21
    type: b1
  - id: b_ocflt_ef_u22
    type: b1
  - id: b_ocflt_ef_u21
    type: b1
  - id: b_flt_rad_u2
    type: b1
  - id: b_flt_fad_u2
    type: b1
  - id: b_flt_eev_u22
    type: b1
  - id: b_flt_eev_u21
    type: b1
  - id: b_flt_eh_u22
    type: b1
  - id: b_flt_eh_u21
    type: b1
  - id: b_scflt_comp_u22
    type: b1
  - id: b_lpflt_comp_u22
    type: b1
  - id: b_flt_expboard_u2
    type: b1
  - id: b_flt_airclean_u2
    type: b1
  - id: b_flt_dftemp_u22
    type: b1
  - id: b_flt_dftemp_u21
    type: b1
  - id: b_flt_rnttemp_u2
    type: b1
  - id: b_flt_suplytemp_u22
    type: b1
  - id: b_flt_suplytemp_u21
    type: b1
  - id: b_flt_frstemp_u2
    type: b1
  - id: msg_reverse_6
    type: b1
  - id: msg_reverse_7
    type: b1
  - id: msg_reverse_8
    type: b1
  - id: msg_reverse_9
    type: b1
  - id: b_flt_mvb_bus
    type: b1
  - id: b_flt_emerg_ivt
    type: b1
  - id: b_flt_seat_temp
    type: b1
  - id: b_flt_veh_temp
    type: b1
