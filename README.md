# README


## citadel.txt
|name|help|type|
|---|---|---|
|citadel_secret_controller_csr_err_count|The number of errors occurred when creating the CSR.|counter|
|citadel_secret_controller_secret_deleted_cert_count|The number of certificates recreated due to secret deletion (service account still exists).|counter|
|citadel_secret_controller_svc_acc_created_cert_count|The number of certificates created due to service account creation.|counter|
|citadel_secret_controller_svc_acc_deleted_cert_count|The number of certificates deleted due to service account deletion.|counter|
|citadel_server_authentication_failure_count|The number of authentication failures.|counter|
|citadel_server_citadel_root_cert_expiry_timestamp|The unix timestamp, in seconds, when Citadel root cert will expire. We set it to negative in case of internal error.|gauge|
|citadel_server_csr_count|The number of CSRs recerived by Citadel server.|counter|
|citadel_server_csr_parsing_err_count|The number of erorrs occurred when parsing the CSR.|counter|
|citadel_server_id_extraction_err_count|The number of errors occurred when extracting the ID from CSR.|counter|
|citadel_server_success_cert_issuance_count|The number of certificates issuances that have succeeded.|counter|
|endpoint_no_pod|Endpoints without an associated pod.|gauge|
|go_gc_duration_seconds|A summary of the GC invocation durations.|summary|
|go_goroutines|Number of goroutines that currently exist.|gauge|
|go_info|Information about the Go environment.|gauge|
|go_memstats_alloc_bytes|Number of bytes allocated and still in use.|gauge|
|go_memstats_alloc_bytes_total|Total number of bytes allocated, even if freed.|counter|
|go_memstats_buck_hash_sys_bytes|Number of bytes used by the profiling bucket hash table.|gauge|
|go_memstats_frees_total|Total number of frees.|counter|
|go_memstats_gc_cpu_fraction|The fraction of this program's available CPU time used by the GC since the program started.|gauge|
|go_memstats_gc_sys_bytes|Number of bytes used for garbage collection system metadata.|gauge|
|go_memstats_heap_alloc_bytes|Number of heap bytes allocated and still in use.|gauge|
|go_memstats_heap_idle_bytes|Number of heap bytes waiting to be used.|gauge|
|go_memstats_heap_inuse_bytes|Number of heap bytes that are in use.|gauge|
|go_memstats_heap_objects|Number of allocated objects.|gauge|
|go_memstats_heap_released_bytes|Number of heap bytes released to OS.|gauge|
|go_memstats_heap_sys_bytes|Number of heap bytes obtained from system.|gauge|
|go_memstats_last_gc_time_seconds|Number of seconds since 1970 of last garbage collection.|gauge|
|go_memstats_lookups_total|Total number of pointer lookups.|counter|
|go_memstats_mallocs_total|Total number of mallocs.|counter|
|go_memstats_mcache_inuse_bytes|Number of bytes in use by mcache structures.|gauge|
|go_memstats_mcache_sys_bytes|Number of bytes used for mcache structures obtained from system.|gauge|
|go_memstats_mspan_inuse_bytes|Number of bytes in use by mspan structures.|gauge|
|go_memstats_mspan_sys_bytes|Number of bytes used for mspan structures obtained from system.|gauge|
|go_memstats_next_gc_bytes|Number of heap bytes when next garbage collection will take place.|gauge|
|go_memstats_other_sys_bytes|Number of bytes used for other system allocations.|gauge|
|go_memstats_stack_inuse_bytes|Number of bytes in use by the stack allocator.|gauge|
|go_memstats_stack_sys_bytes|Number of bytes obtained from system for stack allocator.|gauge|
|go_memstats_sys_bytes|Number of bytes obtained from system.|gauge|
|go_threads|Number of OS threads created.|gauge|
|grpc_server_handled_total|Total number of RPCs completed on the server, regardless of success or failure.|counter|
|grpc_server_handling_seconds|Histogram of response latency (seconds) of gRPC that had been application-level handled by the server.|histogram|
|grpc_server_msg_received_total|Total number of RPC stream messages received on the server.|counter|
|grpc_server_msg_sent_total|Total number of gRPC stream messages sent by the server.|counter|
|grpc_server_started_total|Total number of RPCs started on the server.|counter|
|pilot_conflict_inbound_listener|Number of conflicting inbound listeners.|gauge|
|pilot_conflict_outbound_listener_http_over_current_tcp|Number of conflicting wildcard http listeners with current wildcard tcp listener.|gauge|
|pilot_conflict_outbound_listener_tcp_over_current_http|Number of conflicting wildcard tcp listeners with current wildcard http listener.|gauge|
|pilot_conflict_outbound_listener_tcp_over_current_tcp|Number of conflicting tcp listeners with current tcp listener.|gauge|
|pilot_destrule_subsets|Duplicate subsets across destination rules for same host|gauge|
|pilot_duplicate_envoy_clusters|Duplicate envoy clusters caused by service entries with same hostname|gauge|
|pilot_eds_no_instances|Number of clusters without instances.|gauge|
|pilot_endpoint_not_ready|Endpoint found in unready state.|gauge|
|pilot_no_ip|Pods not found in the endpoint table, possibly invalid.|gauge|
|pilot_vservice_dup_domain|Virtual services with dup domains.|gauge|
|process_cpu_seconds_total|Total user and system CPU time spent in seconds.|counter|
|process_max_fds|Maximum number of open file descriptors.|gauge|
|process_open_fds|Number of open file descriptors.|gauge|
|process_resident_memory_bytes|Resident memory size in bytes.|gauge|
|process_start_time_seconds|Start time of the process since unix epoch in seconds.|gauge|
|process_virtual_memory_bytes|Virtual memory size in bytes.|gauge|
|process_virtual_memory_max_bytes|Maximum amount of virtual memory available in bytes.|gauge|
## envoy.txt
|name|help|type|
|---|---|---|
|envoy_listener_manager_lds_update_attempt||counter|
|envoy_listener_manager_lds_update_success||counter|
|envoy_listener_manager_lds_update_rejected||counter|
|envoy_listener_manager_lds_update_failure||counter|
|envoy_cluster_manager_cds_update_attempt||counter|
|envoy_cluster_manager_cds_update_failure||counter|
|envoy_cluster_manager_cds_update_rejected||counter|
|envoy_cluster_manager_cds_update_success||counter|
|envoy_cluster_http2_header_overflow||counter|
|envoy_cluster_upstream_cx_max_requests||counter|
|envoy_cluster_update_no_rebuild||counter|
|envoy_cluster_lb_subsets_created||counter|
|envoy_cluster_upstream_flow_control_resumed_reading_total||counter|
|envoy_cluster_upstream_cx_destroy_remote||counter|
|envoy_cluster_upstream_cx_destroy_remote_with_active_rq||counter|
|envoy_cluster_upstream_rq_pending_total||counter|
|envoy_cluster_upstream_rq_retry||counter|
|envoy_cluster_lb_healthy_panic||counter|
|envoy_cluster_membership_change||counter|
|envoy_cluster_http2_headers_cb_no_stream||counter|
|envoy_cluster_internal_upstream_rq_completed||counter|
|envoy_cluster_upstream_rq||counter|
|envoy_cluster_upstream_cx_none_healthy||counter|
|envoy_cluster_internal_upstream_rq||counter|
|envoy_cluster_http2_trailers||counter|
|envoy_cluster_lb_zone_routing_sampled||counter|
|envoy_cluster_lb_zone_routing_cross_zone||counter|
|envoy_cluster_lb_subsets_fallback||counter|
|envoy_cluster_lb_zone_number_differs||counter|
|envoy_cluster_upstream_cx_protocol_error||counter|
|envoy_cluster_lb_zone_routing_all_directly||counter|
|envoy_cluster_upstream_cx_connect_attempts_exceeded||counter|
|envoy_cluster_upstream_flow_control_paused_reading_total||counter|
|envoy_cluster_upstream_rq_maintenance_mode||counter|
|envoy_cluster_upstream_cx_connect_timeout||counter|
|envoy_cluster_http2_tx_reset||counter|
|envoy_cluster_update_failure||counter|
|envoy_cluster_upstream_cx_http1_total||counter|
|envoy_cluster_upstream_cx_rx_bytes_total||counter|
|envoy_cluster_lb_subsets_fallback_panic||counter|
|envoy_cluster_update_empty||counter|
|envoy_cluster_upstream_rq_cancelled||counter|
|envoy_cluster_upstream_rq_retry_overflow||counter|
|envoy_cluster_original_dst_host_invalid||counter|
|envoy_cluster_http2_rx_reset||counter|
|envoy_cluster_lb_subsets_selected||counter|
|envoy_cluster_upstream_cx_pool_overflow||counter|
|envoy_cluster_upstream_flow_control_backed_up_total||counter|
|envoy_cluster_lb_zone_no_capacity_left||counter|
|envoy_cluster_upstream_cx_destroy_local_with_active_rq||counter|
|envoy_cluster_upstream_cx_http2_total||counter|
|envoy_cluster_assignment_stale||counter|
|envoy_cluster_upstream_rq_pending_failure_eject||counter|
|envoy_cluster_upstream_rq_timeout||counter|
|envoy_cluster_upstream_cx_close_notify||counter|
|envoy_cluster_upstream_cx_overflow||counter|
|envoy_cluster_upstream_cx_destroy||counter|
|envoy_cluster_upstream_cx_idle_timeout||counter|
|envoy_cluster_upstream_rq_pending_overflow||counter|
|envoy_cluster_upstream_rq_rx_reset||counter|
|envoy_cluster_lb_zone_cluster_too_small||counter|
|envoy_cluster_upstream_rq_retry_success||counter|
|envoy_cluster_lb_recalculate_zone_structures||counter|
|envoy_cluster_upstream_rq_total||counter|
|envoy_cluster_upstream_internal_redirect_succeeded_total||counter|
|envoy_cluster_http2_rx_messaging_error||counter|
|envoy_cluster_assignment_timeout_received||counter|
|envoy_cluster_upstream_internal_redirect_failed_total||counter|
|envoy_cluster_upstream_cx_tx_bytes_total||counter|
|envoy_cluster_upstream_rq_per_try_timeout||counter|
|envoy_cluster_upstream_cx_destroy_with_active_rq||counter|
|envoy_cluster_upstream_flow_control_drained_total||counter|
|envoy_cluster_update_attempt||counter|
|envoy_cluster_upstream_cx_connect_fail||counter|
|envoy_cluster_upstream_cx_destroy_local||counter|
|envoy_cluster_http2_too_many_header_frames||counter|
|envoy_cluster_update_success||counter|
|envoy_cluster_lb_local_cluster_not_ok||counter|
|envoy_cluster_lb_subsets_removed||counter|
|envoy_cluster_bind_errors||counter|
|envoy_cluster_upstream_rq_completed||counter|
|envoy_cluster_upstream_cx_total||counter|
|envoy_cluster_upstream_rq_tx_reset||counter|
|envoy_cluster_retry_or_shadow_abandoned||counter|
|envoy_listener_manager_listener_create_success||counter|
|envoy_listener_manager_listener_create_failure||counter|
|envoy_listener_manager_listener_modified||counter|
|envoy_listener_manager_listener_removed||counter|
|envoy_listener_manager_listener_added||counter|
|envoy_server_watchdog_mega_miss||counter|
|envoy_server_watchdog_miss||counter|
|envoy_cluster_manager_cluster_updated||counter|
|envoy_cluster_manager_cluster_removed||counter|
|envoy_cluster_manager_cluster_updated_via_merge||counter|
|envoy_server_debug_assertion_failures||counter|
|envoy_cluster_manager_update_out_of_merge_window||counter|
|envoy_cluster_manager_cluster_modified||counter|
|envoy_cluster_manager_cluster_added||counter|
|envoy_cluster_manager_update_merge_cancelled||counter|
|envoy_listener_manager_lds_version||gauge|
|envoy_cluster_manager_cds_version||gauge|
|envoy_cluster_circuit_breakers_high_rq_pending_open||gauge|
|envoy_cluster_circuit_breakers_high_rq_retry_open||gauge|
|envoy_cluster_membership_degraded||gauge|
|envoy_cluster_circuit_breakers_default_rq_pending_open||gauge|
|envoy_cluster_circuit_breakers_high_rq_open||gauge|
|envoy_cluster_circuit_breakers_default_cx_open||gauge|
|envoy_cluster_upstream_cx_rx_bytes_buffered||gauge|
|envoy_cluster_upstream_cx_tx_bytes_buffered||gauge|
|envoy_cluster_circuit_breakers_default_rq_open||gauge|
|envoy_cluster_circuit_breakers_default_rq_retry_open||gauge|
|envoy_cluster_membership_excluded||gauge|
|envoy_cluster_circuit_breakers_high_cx_pool_open||gauge|
|envoy_cluster_version||gauge|
|envoy_cluster_circuit_breakers_default_cx_pool_open||gauge|
|envoy_cluster_lb_subsets_active||gauge|
|envoy_cluster_max_host_weight||gauge|
|envoy_cluster_upstream_cx_active||gauge|
|envoy_cluster_membership_healthy||gauge|
|envoy_cluster_membership_total||gauge|
|envoy_cluster_upstream_rq_pending_active||gauge|
|envoy_cluster_upstream_rq_active||gauge|
|envoy_cluster_circuit_breakers_high_cx_open||gauge|
|envoy_listener_manager_total_listeners_active||gauge|
|envoy_listener_manager_total_listeners_warming||gauge|
|envoy_listener_manager_total_listeners_draining||gauge|
|envoy_server_memory_allocated||gauge|
|envoy_server_live||gauge|
|envoy_server_total_connections||gauge|
|envoy_server_concurrency||gauge|
|envoy_server_hot_restart_epoch||gauge|
|envoy_cluster_manager_warming_clusters||gauge|
|envoy_server_uptime||gauge|
|envoy_server_memory_heap_size||gauge|
|envoy_server_days_until_first_cert_expiring||gauge|
|envoy_server_version||gauge|
|envoy_cluster_manager_active_clusters||gauge|
|envoy_server_parent_connections||gauge|
|envoy_cluster_upstream_cx_length_ms||histogram|
|envoy_cluster_upstream_cx_connect_ms||histogram|
## galley.txt
|name|help|type|
|---|---|---|
|endpoint_no_pod|Endpoints without an associated pod.|gauge|
|galley_mcp_source_clients_total|The number of streams currently connected.|gauge|
|galley_mcp_source_message_sizes_bytes|Size of messages received from clients.|histogram|
|galley_mcp_source_recv_failures_total|The number of recv failures in the source.|counter|
|galley_mcp_source_request_acks_total|The number of request acks received by the source.|counter|
|galley_runtime_processor_event_span_duration_milliseconds|The duration between each incoming event|histogram|
|galley_runtime_processor_events_processed_total|The number of events that have been processed|counter|
|galley_runtime_processor_snapshot_events_total|The number of events per snapshot|histogram|
|galley_runtime_processor_snapshot_lifetime_duration_milliseconds|The duration of each snapshot|histogram|
|galley_runtime_processor_snapshots_published_total|The number of snapshots that have been published|counter|
|galley_runtime_state_type_instances_total|The number of type instances per type URL|gauge|
|galley_runtime_strategy_on_change_total|The number of times the strategy's onChange has been called|counter|
|galley_runtime_strategy_timer_max_time_reached_total|The number of times the max time has been reached|counter|
|galley_runtime_strategy_timer_quiesce_reached_total|The number of times a quiesce has been reached|counter|
|galley_runtime_strategy_timer_resets_total|The number of times the timer has been reset|counter|
|galley_source_kube_dynamic_converter_success_total|The number of times a dynamic kubernetes source successfully converted a resource|counter|
|galley_source_kube_event_success_total|The number of times a kubernetes source successfully handled an event|counter|
|galley_validation_cert_key_updates|Galley validation webhook certificate updates|counter|
|galley_validation_config_load|k8s webhook configuration (re)loads|counter|
|galley_validation_config_updates|k8s webhook configuration updates|counter|
|go_gc_duration_seconds|A summary of the GC invocation durations.|summary|
|go_goroutines|Number of goroutines that currently exist.|gauge|
|go_info|Information about the Go environment.|gauge|
|go_memstats_alloc_bytes|Number of bytes allocated and still in use.|gauge|
|go_memstats_alloc_bytes_total|Total number of bytes allocated, even if freed.|counter|
|go_memstats_buck_hash_sys_bytes|Number of bytes used by the profiling bucket hash table.|gauge|
|go_memstats_frees_total|Total number of frees.|counter|
|go_memstats_gc_cpu_fraction|The fraction of this program's available CPU time used by the GC since the program started.|gauge|
|go_memstats_gc_sys_bytes|Number of bytes used for garbage collection system metadata.|gauge|
|go_memstats_heap_alloc_bytes|Number of heap bytes allocated and still in use.|gauge|
|go_memstats_heap_idle_bytes|Number of heap bytes waiting to be used.|gauge|
|go_memstats_heap_inuse_bytes|Number of heap bytes that are in use.|gauge|
|go_memstats_heap_objects|Number of allocated objects.|gauge|
|go_memstats_heap_released_bytes|Number of heap bytes released to OS.|gauge|
|go_memstats_heap_sys_bytes|Number of heap bytes obtained from system.|gauge|
|go_memstats_last_gc_time_seconds|Number of seconds since 1970 of last garbage collection.|gauge|
|go_memstats_lookups_total|Total number of pointer lookups.|counter|
|go_memstats_mallocs_total|Total number of mallocs.|counter|
|go_memstats_mcache_inuse_bytes|Number of bytes in use by mcache structures.|gauge|
|go_memstats_mcache_sys_bytes|Number of bytes used for mcache structures obtained from system.|gauge|
|go_memstats_mspan_inuse_bytes|Number of bytes in use by mspan structures.|gauge|
|go_memstats_mspan_sys_bytes|Number of bytes used for mspan structures obtained from system.|gauge|
|go_memstats_next_gc_bytes|Number of heap bytes when next garbage collection will take place.|gauge|
|go_memstats_other_sys_bytes|Number of bytes used for other system allocations.|gauge|
|go_memstats_stack_inuse_bytes|Number of bytes in use by the stack allocator.|gauge|
|go_memstats_stack_sys_bytes|Number of bytes obtained from system for stack allocator.|gauge|
|go_memstats_sys_bytes|Number of bytes obtained from system.|gauge|
|go_threads|Number of OS threads created.|gauge|
|istio_build|Istio component build info|gauge|
|pilot_conflict_inbound_listener|Number of conflicting inbound listeners.|gauge|
|pilot_conflict_outbound_listener_http_over_current_tcp|Number of conflicting wildcard http listeners with current wildcard tcp listener.|gauge|
|pilot_conflict_outbound_listener_tcp_over_current_http|Number of conflicting wildcard tcp listeners with current wildcard http listener.|gauge|
|pilot_conflict_outbound_listener_tcp_over_current_tcp|Number of conflicting tcp listeners with current tcp listener.|gauge|
|pilot_destrule_subsets|Duplicate subsets across destination rules for same host|gauge|
|pilot_duplicate_envoy_clusters|Duplicate envoy clusters caused by service entries with same hostname|gauge|
|pilot_eds_no_instances|Number of clusters without instances.|gauge|
|pilot_endpoint_not_ready|Endpoint found in unready state.|gauge|
|pilot_no_ip|Pods not found in the endpoint table, possibly invalid.|gauge|
|pilot_vservice_dup_domain|Virtual services with dup domains.|gauge|
|process_cpu_seconds_total|Total user and system CPU time spent in seconds.|counter|
|process_max_fds|Maximum number of open file descriptors.|gauge|
|process_open_fds|Number of open file descriptors.|gauge|
|process_resident_memory_bytes|Resident memory size in bytes.|gauge|
|process_start_time_seconds|Start time of the process since unix epoch in seconds.|gauge|
|process_virtual_memory_bytes|Virtual memory size in bytes.|gauge|
|process_virtual_memory_max_bytes|Maximum amount of virtual memory available in bytes.|gauge|
## mesh.txt
|name|help|type|
|---|---|---|
|istio_request_bytes|request_bytes|histogram|
|istio_request_duration_seconds|request_duration_seconds|histogram|
|istio_requests_total|requests_total|counter|
|istio_response_bytes|response_bytes|histogram|
|istio_tcp_connections_closed_total|tcp_connections_closed_total|counter|
|istio_tcp_connections_opened_total|tcp_connections_opened_total|counter|
|istio_tcp_received_bytes_total|tcp_received_bytes_total|counter|
|istio_tcp_sent_bytes_total|tcp_sent_bytes_total|counter|
## pilot.txt
|name|help|type|
|---|---|---|
|endpoint_no_pod|Endpoints without an associated pod.|gauge|
|go_gc_duration_seconds|A summary of the GC invocation durations.|summary|
|go_goroutines|Number of goroutines that currently exist.|gauge|
|go_info|Information about the Go environment.|gauge|
|go_memstats_alloc_bytes|Number of bytes allocated and still in use.|gauge|
|go_memstats_alloc_bytes_total|Total number of bytes allocated, even if freed.|counter|
|go_memstats_buck_hash_sys_bytes|Number of bytes used by the profiling bucket hash table.|gauge|
|go_memstats_frees_total|Total number of frees.|counter|
|go_memstats_gc_cpu_fraction|The fraction of this program's available CPU time used by the GC since the program started.|gauge|
|go_memstats_gc_sys_bytes|Number of bytes used for garbage collection system metadata.|gauge|
|go_memstats_heap_alloc_bytes|Number of heap bytes allocated and still in use.|gauge|
|go_memstats_heap_idle_bytes|Number of heap bytes waiting to be used.|gauge|
|go_memstats_heap_inuse_bytes|Number of heap bytes that are in use.|gauge|
|go_memstats_heap_objects|Number of allocated objects.|gauge|
|go_memstats_heap_released_bytes|Number of heap bytes released to OS.|gauge|
|go_memstats_heap_sys_bytes|Number of heap bytes obtained from system.|gauge|
|go_memstats_last_gc_time_seconds|Number of seconds since 1970 of last garbage collection.|gauge|
|go_memstats_lookups_total|Total number of pointer lookups.|counter|
|go_memstats_mallocs_total|Total number of mallocs.|counter|
|go_memstats_mcache_inuse_bytes|Number of bytes in use by mcache structures.|gauge|
|go_memstats_mcache_sys_bytes|Number of bytes used for mcache structures obtained from system.|gauge|
|go_memstats_mspan_inuse_bytes|Number of bytes in use by mspan structures.|gauge|
|go_memstats_mspan_sys_bytes|Number of bytes used for mspan structures obtained from system.|gauge|
|go_memstats_next_gc_bytes|Number of heap bytes when next garbage collection will take place.|gauge|
|go_memstats_other_sys_bytes|Number of bytes used for other system allocations.|gauge|
|go_memstats_stack_inuse_bytes|Number of bytes in use by the stack allocator.|gauge|
|go_memstats_stack_sys_bytes|Number of bytes obtained from system for stack allocator.|gauge|
|go_memstats_sys_bytes|Number of bytes obtained from system.|gauge|
|go_threads|Number of OS threads created.|gauge|
|istio_build|Istio component build info|gauge|
|pilot_conflict_inbound_listener|Number of conflicting inbound listeners.|gauge|
|pilot_conflict_outbound_listener_http_over_current_tcp|Number of conflicting wildcard http listeners with current wildcard tcp listener.|gauge|
|pilot_conflict_outbound_listener_tcp_over_current_http|Number of conflicting wildcard tcp listeners with current wildcard http listener.|gauge|
|pilot_conflict_outbound_listener_tcp_over_current_tcp|Number of conflicting tcp listeners with current tcp listener.|gauge|
|pilot_destrule_subsets|Duplicate subsets across destination rules for same host|gauge|
|pilot_duplicate_envoy_clusters|Duplicate envoy clusters caused by service entries with same hostname|gauge|
|pilot_eds_no_instances|Number of clusters without instances.|gauge|
|pilot_endpoint_not_ready|Endpoint found in unready state.|gauge|
|pilot_info|Pilot version and build information.|gauge|
|pilot_invalid_out_listeners|Number of invalid outbound listeners.|gauge|
|pilot_k8s_reg_events|Events from k8s registry.|counter|
|pilot_mcp_sink_reconnections|The number of times the sink has reconnected.|counter|
|pilot_mcp_sink_recv_failures_total|The number of recv failures in the source.|counter|
|pilot_mcp_sink_request_acks_total|The number of request acks received by the source.|counter|
|pilot_no_ip|Pods not found in the endpoint table, possibly invalid.|gauge|
|pilot_proxy_convergence_time|Delay between config change and all proxies converging.|histogram|
|pilot_rds_expired_nonce|Total number of RDS messages with an expired nonce.|counter|
|pilot_services|Total services known to pilot.|gauge|
|pilot_total_xds_internal_errors|Total number of internal XDS errors in pilot (check logs).|counter|
|pilot_total_xds_rejects|Total number of XDS responses from pilot rejected by proxy.|counter|
|pilot_virt_services|Total virtual services known to pilot.|gauge|
|pilot_vservice_dup_domain|Virtual services with dup domains.|gauge|
|pilot_xds|Number of endpoints connected to this pilot using XDS.|gauge|
|pilot_xds_eds_instances|Instances for each cluster, as of last push. Zero instances is an error.|gauge|
|pilot_xds_push_context_errors|Number of errors (timeouts) initiating push context.|counter|
|pilot_xds_push_errors|Number of errors (timeouts) pushing to sidecars.|counter|
|pilot_xds_push_timeout|Pilot push timeout, will retry.|counter|
|pilot_xds_push_timeout_failures|Pilot push timeout failures after repeated attempts.|counter|
|pilot_xds_pushes|Pilot build and send errors for lds, rds, cds and eds.|counter|
|pilot_xds_write_timeout|Pilot XDS response write timeouts.|counter|
|process_cpu_seconds_total|Total user and system CPU time spent in seconds.|counter|
|process_max_fds|Maximum number of open file descriptors.|gauge|
|process_open_fds|Number of open file descriptors.|gauge|
|process_resident_memory_bytes|Resident memory size in bytes.|gauge|
|process_start_time_seconds|Start time of the process since unix epoch in seconds.|gauge|
|process_virtual_memory_bytes|Virtual memory size in bytes.|gauge|
|process_virtual_memory_max_bytes|Maximum amount of virtual memory available in bytes.|gauge|
## policy.txt
|name|help|type|
|---|---|---|
|go_gc_duration_seconds|A summary of the GC invocation durations.|summary|
|go_goroutines|Number of goroutines that currently exist.|gauge|
|go_info|Information about the Go environment.|gauge|
|go_memstats_alloc_bytes|Number of bytes allocated and still in use.|gauge|
|go_memstats_alloc_bytes_total|Total number of bytes allocated, even if freed.|counter|
|go_memstats_buck_hash_sys_bytes|Number of bytes used by the profiling bucket hash table.|gauge|
|go_memstats_frees_total|Total number of frees.|counter|
|go_memstats_gc_cpu_fraction|The fraction of this program's available CPU time used by the GC since the program started.|gauge|
|go_memstats_gc_sys_bytes|Number of bytes used for garbage collection system metadata.|gauge|
|go_memstats_heap_alloc_bytes|Number of heap bytes allocated and still in use.|gauge|
|go_memstats_heap_idle_bytes|Number of heap bytes waiting to be used.|gauge|
|go_memstats_heap_inuse_bytes|Number of heap bytes that are in use.|gauge|
|go_memstats_heap_objects|Number of allocated objects.|gauge|
|go_memstats_heap_released_bytes|Number of heap bytes released to OS.|gauge|
|go_memstats_heap_sys_bytes|Number of heap bytes obtained from system.|gauge|
|go_memstats_last_gc_time_seconds|Number of seconds since 1970 of last garbage collection.|gauge|
|go_memstats_lookups_total|Total number of pointer lookups.|counter|
|go_memstats_mallocs_total|Total number of mallocs.|counter|
|go_memstats_mcache_inuse_bytes|Number of bytes in use by mcache structures.|gauge|
|go_memstats_mcache_sys_bytes|Number of bytes used for mcache structures obtained from system.|gauge|
|go_memstats_mspan_inuse_bytes|Number of bytes in use by mspan structures.|gauge|
|go_memstats_mspan_sys_bytes|Number of bytes used for mspan structures obtained from system.|gauge|
|go_memstats_next_gc_bytes|Number of heap bytes when next garbage collection will take place.|gauge|
|go_memstats_other_sys_bytes|Number of bytes used for other system allocations.|gauge|
|go_memstats_stack_inuse_bytes|Number of bytes in use by the stack allocator.|gauge|
|go_memstats_stack_sys_bytes|Number of bytes obtained from system for stack allocator.|gauge|
|go_memstats_sys_bytes|Number of bytes obtained from system.|gauge|
|go_threads|Number of OS threads created.|gauge|
|grpc_io_server_completed_rpcs|Count of RPCs by method and status.|counter|
|grpc_io_server_received_bytes_per_rpc|Distribution of received bytes per RPC, by method.|histogram|
|grpc_io_server_sent_bytes_per_rpc|Distribution of total sent bytes per RPC, by method.|histogram|
|grpc_io_server_server_latency|Distribution of server latency in milliseconds, by method.|histogram|
|istio_build|Istio component build info|gauge|
|mixer_config_adapter_info_config_errors_total|The number of errors encountered during processing of the adapter info configuration.|gauge|
|mixer_config_adapter_info_configs_total|The number of known adapters in the current config.|gauge|
|mixer_config_attributes_total|The number of known attributes in the current config.|gauge|
|mixer_config_handler_configs_total|The number of known handlers in the current config.|gauge|
|mixer_config_handler_validation_error_total|The number of errors encountered because handler validation returned error.|gauge|
|mixer_config_instance_config_errors_total|The number of errors encountered during processing of the instance configuration.|gauge|
|mixer_config_instance_configs_total|The number of known instances in the current config.|gauge|
|mixer_config_rule_config_errors_total|The number of errors encountered during processing of the rule configuration.|gauge|
|mixer_config_rule_config_match_error_total|The number of rule conditions that was not parseable.|gauge|
|mixer_config_rule_configs_total|The number of known rules in the current config.|gauge|
|mixer_config_template_config_errors_total|The number of errors encountered during processing of the template configuration.|gauge|
|mixer_config_template_configs_total|The number of known templates in the current config.|gauge|
|mixer_config_unsatisfied_action_handler_total|The number of actions that failed due to handlers being unavailable.|gauge|
|mixer_dispatcher_destinations_per_request|Number of handlers dispatched per request by Mixer|histogram|
|mixer_dispatcher_destinations_per_variety_total|Number of Mixer adapter destinations by template variety type|gauge|
|mixer_dispatcher_instances_per_request|Number of instances created per request by Mixer|histogram|
|mixer_handler_closed_handlers_total|The number of handlers that were closed during config transition.|gauge|
|mixer_handler_daemons_total|The current number of active daemon routines in a given adapter environment.|gauge|
|mixer_handler_handler_build_failures_total|The number of handlers that failed creation during config transition.|gauge|
|mixer_handler_handler_close_failures_total|The number of errors encountered while closing handlers during config transition.|gauge|
|mixer_handler_new_handlers_total|The number of handlers that were newly created during config transition.|gauge|
|mixer_handler_reused_handlers_total|The number of handlers that were re-used during config transition.|gauge|
|mixer_mcp_sink_reconnections|The number of times the sink has reconnected.|counter|
|mixer_mcp_sink_recv_failures_total|The number of recv failures in the source.|counter|
|mixer_mcp_sink_request_acks_total|The number of request acks received by the source.|counter|
|mixer_runtime_dispatch_duration_seconds|Duration in seconds for adapter dispatches handled by Mixer.|histogram|
|mixer_runtime_dispatches_total|Total number of adapter dispatches handled by Mixer.|counter|
|process_cpu_seconds_total|Total user and system CPU time spent in seconds.|counter|
|process_max_fds|Maximum number of open file descriptors.|gauge|
|process_open_fds|Number of open file descriptors.|gauge|
|process_resident_memory_bytes|Resident memory size in bytes.|gauge|
|process_start_time_seconds|Start time of the process since unix epoch in seconds.|gauge|
|process_virtual_memory_bytes|Virtual memory size in bytes.|gauge|
|process_virtual_memory_max_bytes|Maximum amount of virtual memory available in bytes.|gauge|
## telemetry.txt
|name|help|type|
|---|---|---|
|go_gc_duration_seconds|A summary of the GC invocation durations.|summary|
|go_goroutines|Number of goroutines that currently exist.|gauge|
|go_info|Information about the Go environment.|gauge|
|go_memstats_alloc_bytes|Number of bytes allocated and still in use.|gauge|
|go_memstats_alloc_bytes_total|Total number of bytes allocated, even if freed.|counter|
|go_memstats_buck_hash_sys_bytes|Number of bytes used by the profiling bucket hash table.|gauge|
|go_memstats_frees_total|Total number of frees.|counter|
|go_memstats_gc_cpu_fraction|The fraction of this program's available CPU time used by the GC since the program started.|gauge|
|go_memstats_gc_sys_bytes|Number of bytes used for garbage collection system metadata.|gauge|
|go_memstats_heap_alloc_bytes|Number of heap bytes allocated and still in use.|gauge|
|go_memstats_heap_idle_bytes|Number of heap bytes waiting to be used.|gauge|
|go_memstats_heap_inuse_bytes|Number of heap bytes that are in use.|gauge|
|go_memstats_heap_objects|Number of allocated objects.|gauge|
|go_memstats_heap_released_bytes|Number of heap bytes released to OS.|gauge|
|go_memstats_heap_sys_bytes|Number of heap bytes obtained from system.|gauge|
|go_memstats_last_gc_time_seconds|Number of seconds since 1970 of last garbage collection.|gauge|
|go_memstats_lookups_total|Total number of pointer lookups.|counter|
|go_memstats_mallocs_total|Total number of mallocs.|counter|
|go_memstats_mcache_inuse_bytes|Number of bytes in use by mcache structures.|gauge|
|go_memstats_mcache_sys_bytes|Number of bytes used for mcache structures obtained from system.|gauge|
|go_memstats_mspan_inuse_bytes|Number of bytes in use by mspan structures.|gauge|
|go_memstats_mspan_sys_bytes|Number of bytes used for mspan structures obtained from system.|gauge|
|go_memstats_next_gc_bytes|Number of heap bytes when next garbage collection will take place.|gauge|
|go_memstats_other_sys_bytes|Number of bytes used for other system allocations.|gauge|
|go_memstats_stack_inuse_bytes|Number of bytes in use by the stack allocator.|gauge|
|go_memstats_stack_sys_bytes|Number of bytes obtained from system for stack allocator.|gauge|
|go_memstats_sys_bytes|Number of bytes obtained from system.|gauge|
|go_threads|Number of OS threads created.|gauge|
|grpc_io_server_completed_rpcs|Count of RPCs by method and status.|counter|
|grpc_io_server_received_bytes_per_rpc|Distribution of received bytes per RPC, by method.|histogram|
|grpc_io_server_sent_bytes_per_rpc|Distribution of total sent bytes per RPC, by method.|histogram|
|grpc_io_server_server_latency|Distribution of server latency in milliseconds, by method.|histogram|
|istio_build|Istio component build info|gauge|
|mixer_config_adapter_info_config_errors_total|The number of errors encountered during processing of the adapter info configuration.|gauge|
|mixer_config_adapter_info_configs_total|The number of known adapters in the current config.|gauge|
|mixer_config_attributes_total|The number of known attributes in the current config.|gauge|
|mixer_config_handler_configs_total|The number of known handlers in the current config.|gauge|
|mixer_config_handler_validation_error_total|The number of errors encountered because handler validation returned error.|gauge|
|mixer_config_instance_config_errors_total|The number of errors encountered during processing of the instance configuration.|gauge|
|mixer_config_instance_configs_total|The number of known instances in the current config.|gauge|
|mixer_config_rule_config_errors_total|The number of errors encountered during processing of the rule configuration.|gauge|
|mixer_config_rule_config_match_error_total|The number of rule conditions that was not parseable.|gauge|
|mixer_config_rule_configs_total|The number of known rules in the current config.|gauge|
|mixer_config_template_config_errors_total|The number of errors encountered during processing of the template configuration.|gauge|
|mixer_config_template_configs_total|The number of known templates in the current config.|gauge|
|mixer_config_unsatisfied_action_handler_total|The number of actions that failed due to handlers being unavailable.|gauge|
|mixer_dispatcher_destinations_per_request|Number of handlers dispatched per request by Mixer|histogram|
|mixer_dispatcher_destinations_per_variety_total|Number of Mixer adapter destinations by template variety type|gauge|
|mixer_dispatcher_instances_per_request|Number of instances created per request by Mixer|histogram|
|mixer_handler_closed_handlers_total|The number of handlers that were closed during config transition.|gauge|
|mixer_handler_daemons_total|The current number of active daemon routines in a given adapter environment.|gauge|
|mixer_handler_handler_build_failures_total|The number of handlers that failed creation during config transition.|gauge|
|mixer_handler_handler_close_failures_total|The number of errors encountered while closing handlers during config transition.|gauge|
|mixer_handler_new_handlers_total|The number of handlers that were newly created during config transition.|gauge|
|mixer_handler_reused_handlers_total|The number of handlers that were re-used during config transition.|gauge|
|mixer_mcp_sink_reconnections|The number of times the sink has reconnected.|counter|
|mixer_mcp_sink_recv_failures_total|The number of recv failures in the source.|counter|
|mixer_mcp_sink_request_acks_total|The number of request acks received by the source.|counter|
|mixer_runtime_dispatch_duration_seconds|Duration in seconds for adapter dispatches handled by Mixer.|histogram|
|mixer_runtime_dispatches_total|Total number of adapter dispatches handled by Mixer.|counter|
|process_cpu_seconds_total|Total user and system CPU time spent in seconds.|counter|
|process_max_fds|Maximum number of open file descriptors.|gauge|
|process_open_fds|Number of open file descriptors.|gauge|
|process_resident_memory_bytes|Resident memory size in bytes.|gauge|
|process_start_time_seconds|Start time of the process since unix epoch in seconds.|gauge|
|process_virtual_memory_bytes|Virtual memory size in bytes.|gauge|
|process_virtual_memory_max_bytes|Maximum amount of virtual memory available in bytes.|gauge|
