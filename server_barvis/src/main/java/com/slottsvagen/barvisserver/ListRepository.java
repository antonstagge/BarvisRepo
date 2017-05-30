package com.slottsvagen.barvisserver;

import org.springframework.data.repository.CrudRepository;

/**
 * Represents a repository containing different list entities.
 *
 * @author Fredrik Omstedt
 */
public interface ListRepository extends CrudRepository<List, Long> {
}
