package com.slottsvagen.barvisserver;

import lombok.Data;

import javax.persistence.*;
import javax.validation.constraints.NotNull;

/**
 * Represents a list element in the database. Each list element is connected to a list
 * and represents one of the entities within that list.
 *
 * @author Fredrik Omstedt
 */
@Data
@Entity
@Table(name = "ListElement")
public class ListElement {
    private @Id @GeneratedValue long listElementId;
    private @NotNull String name;

    @JoinColumn(name = "list")
    @ManyToOne
    private @NotNull List list;

    public ListElement() {

    }
}
